from sympy import atan as atan, cos as cos, diff as diff, pi as pi, sin as sin
from sympy.core.symbol import Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.matrices import Matrix as Matrix
from sympy.solvers.solveset import linsolve as linsolve

class Cable:
    def __init__(self, support_1, support_2) -> None: ...
    @property
    def supports(self): ...
    @property
    def left_support(self): ...
    @property
    def right_support(self): ...
    @property
    def loads(self): ...
    @property
    def loads_position(self): ...
    @property
    def length(self): ...
    @property
    def reaction_loads(self): ...
    @property
    def tension(self): ...
    def tension_at(self, x): ...
    def apply_length(self, length) -> None: ...
    def change_support(self, label, new_support) -> None: ...
    def apply_load(self, order, load) -> None: ...
    def remove_loads(self, *args) -> None: ...
    def solve(self, *args): ...
