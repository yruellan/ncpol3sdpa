from typing import List, Tuple

import numpy as np
import sympy
from scipy.sparse import lil_matrix

from ncpol3sdpa.resolution import AlgebraSDP, ConstraintGroup
from ncpol3sdpa.sdp_repr import (
    EqConstraint,
    MomentMatrixSDP,
    ProblemSDP,
    InequalityScalarConstraint,
)


def algebra_to_SDP_add_equality_constraint(
    problem: ProblemSDP, algebra: AlgebraSDP, eq_constraint: ConstraintGroup
) -> None:
    implied_constraints = eq_constraint.zero_polynomials
    for implied_constraint in implied_constraints:
        # constraint matrix
        a_0 = algebra.polynomial_to_matrix(implied_constraint, real_part=True)
        constraint = EqConstraint([(problem.MOMENT_MATRIX_VAR_NUM, a_0)])
        problem.constraints.append(constraint)

        if not algebra.is_real:
            b_0 = algebra.polynomial_to_matrix(implied_constraint, real_part=False)
            constraint = EqConstraint([(problem.MOMENT_MATRIX_VAR_NUM, b_0)])
            problem.constraints.append(constraint)


def add_inequality_sub_constraint(
    problem: ProblemSDP,
    algebra: AlgebraSDP,
    poly: sympy.Expr,
    constraint_matrix_size: int,
    i: int,
    j: int,
    new_var_idx: int,
) -> None:
    """Sets a constraints on a PSD variable to make it represent that inequality constraint"""
    dtype = np.float64 if problem.is_real else np.complex64

    # real part constraint
    a_k = lil_matrix((constraint_matrix_size, constraint_matrix_size), dtype=dtype)  # type:ignore
    a_k[i, j] -= 0.5
    a_k[j, i] -= 0.5

    a_0 = algebra.polynomial_to_matrix(poly, real_part=True)
    constraint = EqConstraint(
        [(problem.MOMENT_MATRIX_VAR_NUM, a_0), (new_var_idx, a_k)]
    )
    problem.constraints.append(constraint)

    # imaginary part contraint
    if not algebra.is_real:
        b_k = lil_matrix((constraint_matrix_size, constraint_matrix_size), dtype=dtype)  # type:ignore
        b_k[i, j] -= 0.5j
        b_k[j, i] += 0.5j

        b_0 = algebra.polynomial_to_matrix(poly, real_part=False)
        constraint = EqConstraint(
            [(problem.MOMENT_MATRIX_VAR_NUM, b_0), (new_var_idx, b_k)]
        )
        problem.constraints.append(constraint)


def algebra_to_SDP_add_inequality_constraint(
    problem: ProblemSDP,
    algebra: AlgebraSDP,
    constraint_moment_matrix: List[List[sympy.Expr]],
) -> None:
    """Adds the translation of an inequality constraint"""
    constraint_matrix_size = len(constraint_moment_matrix)

    new_var = len(problem.variable_sizes)
    problem.variable_sizes.append(constraint_matrix_size)

    for i, row in enumerate(constraint_moment_matrix):
        for j, poly in enumerate(row):
            add_inequality_sub_constraint(
                problem, algebra, poly, constraint_matrix_size, i, j, new_var
            )


def algebra_to_SDP_add_local_inequality_constraint(
    problem: ProblemSDP,
    algebra: AlgebraSDP,
    local_constraint: sympy.Expr,
) -> None:
    "Adds a local inequality constraint(trace) to the algebra"
    a_0 = algebra.polynomial_to_matrix(local_constraint)
    constraint = InequalityScalarConstraint((problem.MOMENT_MATRIX_VAR_NUM, a_0))
    problem.inequality_scalar_constraints.append(constraint)


def algebra_to_SDP(algebra: AlgebraSDP) -> ProblemSDP:
    """Convert the algebraic representation to the numeric SDP representation"""

    moment_matrix_size = len(algebra.moment_matrix)

    # Convert objective
    objective = algebra.polynomial_to_matrix(algebra.objective)

    # Moment matrix
    equiv_classes: List[List[Tuple[int, int]]] = list(
        algebra.monomial_to_positions.values()
    )

    moment_matrix_repr = MomentMatrixSDP(moment_matrix_size, equiv_classes)

    result_SDP = ProblemSDP(moment_matrix_repr, objective, is_real=algebra.is_real)

    # Translate Equality constraints

    for eq_constraint in algebra.equality_constraints:
        algebra_to_SDP_add_equality_constraint(result_SDP, algebra, eq_constraint)

    # Translate Inequality constrains

    for constraint_matrix in algebra.constraint_moment_matrices:
        algebra_to_SDP_add_inequality_constraint(result_SDP, algebra, constraint_matrix)

    # Translate Local inequality constraints
    for local_constraint in algebra.local_inequality_constraints:
        algebra_to_SDP_add_local_inequality_constraint(
            result_SDP, algebra, local_constraint
        )

    return result_SDP
