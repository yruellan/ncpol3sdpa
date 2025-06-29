from _typeshed import Incomplete
from sympy.abc import x as x, y as y, z as z
from sympy.core import Expr as Expr, S as S, Symbol as Symbol, diff as diff
from sympy.geometry import Point as Point, Point2D as Point2D, Polygon as Polygon, Segment2D as Segment2D
from sympy.polys.polytools import LC as LC, Poly as Poly, degree_list as degree_list, gcd_list as gcd_list
from sympy.simplify.simplify import nsimplify as nsimplify

def polytope_integrate(poly, expr: Incomplete | None = None, *, clockwise: bool = False, max_degree: Incomplete | None = None): ...
def strip(monom): ...
def main_integrate3d(expr, facets, vertices, hp_params, max_degree: Incomplete | None = None): ...
def main_integrate(expr, facets, hp_params, max_degree: Incomplete | None = None): ...
def polygon_integrate(facet, hp_param, index, facets, vertices, expr, degree): ...
def distance_to_side(point, line_seg, A): ...
def lineseg_integrate(polygon, index, line_seg, expr, degree): ...
def integration_reduction(facets, index, a, b, expr, dims, degree): ...
def left_integral2D(m, index, facets, x0, expr, gens): ...
def integration_reduction_dynamic(facets, index, a, b, expr, degree, dims, x_index, y_index, max_index, x0, monomial_values, monom_index, vertices: Incomplete | None = None, hp_param: Incomplete | None = None): ...
def left_integral3D(facets, index, expr, vertices, hp_param, degree): ...
def gradient_terms(binomial_power: int = 0, no_of_gens: int = 2): ...
def hyperplane_parameters(poly, vertices: Incomplete | None = None): ...
def cross_product(v1, v2, v3): ...
def best_origin(a, b, lineseg, expr): ...
def decompose(expr, separate: bool = False): ...
def point_sort(poly, normal: Incomplete | None = None, clockwise: bool = True): ...
def norm(point): ...
def intersection(geom_1, geom_2, intersection_type): ...
def is_vertex(ent): ...
def plot_polytope(poly) -> None: ...
def plot_polynomial(expr) -> None: ...
