from typing import List, NamedTuple, Tuple, Any
from collections.abc import Callable

import sympy
import numpy
from numpy.typing import NDArray
from ncpol3sdpa.sdp_solution import Solution_SDP
from ncpol3sdpa.resolution import AlgebraSDP
from ncpol3sdpa.resolution.utils import sympy_sum
from .solution_real_to_complex import solution_real_to_complex


def semidefinite_PTP_decomp(A: NDArray[numpy.float64]) -> NDArray[numpy.float64]:
    """Returns $P$ such that $A = P^† P$ .

    We could not use the standard Cholesky decomposition of numpy, because it does not like singular
    positive semidefinite matrices(it only works with positive definite ones).
    """
    eigenvalues, eigenvectors = numpy.linalg.eigh(A)
    # Clip small negative values (numerical errors)
    eigvals_clipped = numpy.clip(eigenvalues, 0, None)
    sqrt_eigvals = numpy.sqrt(eigvals_clipped)

    P = eigenvectors @ numpy.diag(sqrt_eigvals)
    return numpy.conj(P).T  # type: ignore


class SumOfMultiplesPolynomial(NamedTuple):
    """Represents an Equality constraint polynomial"""

    """The zero polynomial"""
    poly: sympy.Expr

    """Terms that multiply the polynomial"""
    multiplier_monomials: List[Tuple[sympy.Expr, sympy.Expr]]

    """Function that maps a monomial to it's adjoint (in particular in the complex case)"""
    adjoint_func: Callable[[sympy.Expr], sympy.Expr]

    def to_expression(self) -> sympy.Expr:
        # fmt: off
        terms: map[sympy.Expr] = map(
            lambda multiplier:
            self.adjoint_func(multiplier[0])
            * self.poly
            * multiplier[1],
            self.multiplier_monomials,
        )
        # fmt: on
        return sympy_sum(terms)


class SumOfSquares:
    """Data structure representing a sum of squares polynomials"""

    def __init__(
        self,
        squares: List[sympy.Expr],
        middle_term: sympy.Expr,
        adjoint_func: Callable[[sympy.Expr], sympy.Expr],
    ) -> None:
        """The polynomial represented is the sum of the squares of the elements of `squares`"""
        self.squares = squares
        self.middle_term = middle_term
        self.adjoint_func = adjoint_func

    def to_expression(self) -> sympy.Expr:
        return sympy_sum(
            [self.adjoint_func(term) * self.middle_term * term for term in self.squares]
        )


class SosDecomposition:
    """Class to represent the SOS problem"""

    def __init__(
        self,
        dual_objective: float,
        SOS: SumOfSquares,
        SOS_i: List[SumOfSquares],
        eq_polys: List[SumOfMultiplesPolynomial],  # $\\nu_i * f_i | \\eta_i * h_i
        original_objective: sympy.Expr,
    ) -> None:
        self.dual_objective = dual_objective
        self.SOS = SOS
        self.SOS_i = SOS_i
        self.eq_polys = eq_polys
        self.original_objective = original_objective

    # TODO add substitution rules
    def reconstructed_objective(self) -> sympy.Expr:
        """
        Calculates the objective polynomial from the SOS formula
        See equation (34) form "Semidefinite programming relaxations for quantum correlations"

        Note:
        THIS FUNCTION TAKES A LOT OF TIME TO COMPUTE
        """

        s_lambda: sympy.Expr = sympy.sympify(self.dual_objective)
        return sympy_sum(
            [s_lambda, -self.SOS.to_expression()]
            + [-sos.to_expression() for sos in self.SOS_i]
            + [-cpol.to_expression() for cpol in self.eq_polys]
        )

    def objective_error(self) -> float:
        """Returns the maximum difference in coefficients of f - f_reconstructed,
        where f is the objective polynomial, and f_reconstructed is the reconstructed
        objective, see the `reconstructed_objective` function above.

        Ideally, this should be zero. In practice it is non zero due to numerical precision."""
        difference: sympy.Expr = sympy.expand(
            self.original_objective - self.reconstructed_objective()
        )
        epsilon = 0.0
        for v in difference.as_coefficients_dict().values():
            epsilon = max(epsilon, abs(v))

        return epsilon


def compute_equality_constraints(
    problem_algebra: AlgebraSDP, solution: Solution_SDP[numpy.float64]
) -> List[SumOfMultiplesPolynomial]:
    """Obtain equality constraint data from the solution"""

    # `solution.dual_eqC_variables` contains the constraints in order
    # for each equality contraint is f_i = 0 has a group of sub-constraints :
    #   {m* f_i *n = 0 | m,n monomials}
    # `solution.dual_eqC_variables` has  the dual variables of sub constraints in the following order:
    #  * first, the sub-constraints of f_0, with the order indicated by constraint.monomial_multiples
    #  * then, the sub-constraints of f_1,
    #  * etc...

    y_idx = 0
    res = []
    for constraint in problem_algebra.equality_constraints:
        multiplier_monomials: List[Tuple[sympy.Expr, sympy.Expr]] = []
        for monomials in constraint.monomial_multiples:
            a, b = monomials
            nu_i = solution.dual_eqC_variables[y_idx]
            y_idx += 1
            multiplier_monomials.append(
                (0.5 * nu_i * problem_algebra.get_adjoint(a), b)
            )
            multiplier_monomials.append(
                (0.5 * nu_i * problem_algebra.get_adjoint(b), a)
            )

            if not problem_algebra.is_real:
                nu_i2 = solution.dual_eqC_variables[y_idx]
                y_idx += 1
                multiplier_monomials.append(
                    (-0.5j * nu_i2 * problem_algebra.get_adjoint(a), b)
                )
                multiplier_monomials.append(
                    (+0.5j * nu_i2 * problem_algebra.get_adjoint(b), a)
                )

        res.append(
            SumOfMultiplesPolynomial(
                constraint.zero_polynomials[0],
                multiplier_monomials,
                adjoint_func=problem_algebra.get_adjoint,
            )
        )

    for i in range(len(problem_algebra.local_inequality_constraints)):
        multiplier_monomials = [(sympy.S.One, sympy.S.One)]
        poly = problem_algebra.local_inequality_constraints[i]
        res.append(
            SumOfMultiplesPolynomial(
                poly, multiplier_monomials, adjoint_func=problem_algebra.get_adjoint
            )
        )

    return res


def compute_sos_decomposition(
    problem_algebra: AlgebraSDP, solution: Solution_SDP[Any]
) -> SosDecomposition:
    """Computes an SOS decomposition of (objective polynomial - lambda) using of the solution to the
    dual SDP.

    returns: (lambda, SOS, [SOS_i | i in range(len(algebra.constraints))])
    requires: solution is a solution of the SDP relaxation
    ensures: lambda - problem_algebra.objective_polynomial = SOS + Sum of(SOS_i*g_i)
    """
    if not problem_algebra.is_real:
        solution = solution_real_to_complex(solution)
    A = solution.dual_PSD_variables[0]
    B = solution.dual_PSD_variables[1:]

    def calculate_SOS(
        w: List[sympy.Expr], A: NDArray[numpy.float64], middle: sympy.Expr
    ) -> SumOfSquares:
        """
        w† A w is a polynomial, and if A is positive-semidefinite, then
        this function will calculate the SOS of this polynomial using the
        eigenvalue decomposition
        Arguments:
        w is the vector of monomials from AlgebraSDP
        A is the numerical result of the dual variable from the SDP
        """
        P = semidefinite_PTP_decomp(A)
        Pw: List[sympy.Expr] = [sympy.S.Zero for _ in range(len(P))]
        for i in range(len(P)):
            for j in range(len(P)):
                Pw[i] += P[i][j] * w[j]
        return SumOfSquares(Pw, middle, adjoint_func=problem_algebra.get_adjoint)

    w = problem_algebra.monomials  # list of monomials used in the polynomial
    SOS = calculate_SOS(w, A, sympy.S.One)

    SOSi = [
        calculate_SOS(w, B[i], problem_algebra.psd_polynomials_gi[i])
        for i in range(len(B))
    ]

    eq_polys = compute_equality_constraints(problem_algebra, solution)

    return SosDecomposition(
        solution.dual_objective_value,
        SOS,
        SOSi,
        eq_polys,
        original_objective=problem_algebra.objective,
    )
