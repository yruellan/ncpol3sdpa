from _typeshed import Incomplete
from sympy.core import Rational as Rational, S as S, sympify as sympify
from sympy.core.function import expand_mul as expand_mul
from sympy.discrete.transforms import fft as fft, fwht as fwht, ifft as ifft, ifwht as ifwht, intt as intt, inverse_mobius_transform as inverse_mobius_transform, mobius_transform as mobius_transform, ntt as ntt
from sympy.external.gmpy import MPZ as MPZ, lcm as lcm
from sympy.utilities.iterables import iterable as iterable
from sympy.utilities.misc import as_int as as_int

def convolution(a, b, cycle: int = 0, dps: Incomplete | None = None, prime: Incomplete | None = None, dyadic: Incomplete | None = None, subset: Incomplete | None = None): ...
def convolution_fft(a, b, dps: Incomplete | None = None): ...
def convolution_ntt(a, b, prime): ...
def convolution_fwht(a, b): ...
def convolution_subset(a, b): ...
def covering_product(a, b): ...
def intersecting_product(a, b): ...
def convolution_int(a, b): ...
