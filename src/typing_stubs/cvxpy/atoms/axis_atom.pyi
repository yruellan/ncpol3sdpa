import abc
from _typeshed import Incomplete
from cvxpy.atoms.atom import Atom as Atom

class AxisAtom(Atom, metaclass=abc.ABCMeta):
    axis: Incomplete
    keepdims: Incomplete
    def __init__(self, expr, axis: int | None = None, keepdims: bool = False) -> None: ...
    def shape_from_args(self) -> tuple[int, ...]: ...
    def get_data(self): ...
    def validate_arguments(self) -> None: ...
