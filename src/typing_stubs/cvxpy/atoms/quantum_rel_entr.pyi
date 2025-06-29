from _typeshed import Incomplete
from cvxpy.atoms.atom import Atom as Atom
from cvxpy.constraints.constraint import Constraint as Constraint

class quantum_rel_entr(Atom):
    quad_approx: Incomplete
    def __init__(self, X, Y, quad_approx: tuple[int, int] = (3, 3)) -> None: ...
    def numeric(self, values): ...
    def validate_arguments(self) -> None: ...
    def sign_from_args(self) -> tuple[bool, bool]: ...
    def is_atom_convex(self) -> bool: ...
    def shape_from_args(self) -> tuple[int, ...]: ...
    def is_atom_concave(self) -> bool: ...
    def is_incr(self, idx) -> bool: ...
    def is_decr(self, idx) -> bool: ...
    def get_data(self): ...
