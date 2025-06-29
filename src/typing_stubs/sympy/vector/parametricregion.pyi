from sympy.core import Basic as Basic, Tuple as Tuple
from sympy.core.numbers import pi as pi
from sympy.functions.elementary.trigonometric import tan as tan
from sympy.geometry import Curve as Curve, Ellipse as Ellipse, Point as Point, Polygon as Polygon, Segment as Segment
from sympy.simplify import trigsimp as trigsimp
from sympy.solvers import solve as solve
from sympy.vector import ImplicitRegion as ImplicitRegion

class ParametricRegion(Basic):
    def __new__(cls, definition, *bounds): ...
    @property
    def definition(self): ...
    @property
    def limits(self): ...
    @property
    def parameters(self): ...
    @property
    def dimensions(self): ...

def parametric_region_list(reg) -> None: ...
def _(obj): ...
