from _typeshed import Incomplete
from cvxpy.error import SolverError as SolverError
from cvxpy.reductions.solution import Solution as Solution, failure_solution as failure_solution
from cvxpy.reductions.solvers.conic_solvers.conic_solver import ConicSolver as ConicSolver, dims_to_solver_dict as dims_to_solver_dict

class HIGHS(ConicSolver):
    MIP_CAPABLE: bool
    SUPPORTED_CONSTRAINTS: Incomplete
    MI_SUPPORTED_CONSTRAINTS = SUPPORTED_CONSTRAINTS
    STATUS_MAP: Incomplete
    def name(self): ...
    def import_solver(self) -> None: ...
    def accepts(self, problem) -> bool: ...
    def apply(self, problem): ...
    def invert(self, results, inverse_data): ...
    def solve_via_data(self, data, warm_start: bool, verbose: bool, solver_opts, solver_cache: Incomplete | None = None): ...
