from sympy.core.containers import Tuple as Tuple
from sympy.core.numbers import Integer as Integer, Rational as Rational
from sympy.core.singleton import S as S

def egyptian_fraction(r, algorithm: str = 'Greedy'): ...
def egypt_greedy(x, y): ...
def egypt_graham_jewett(x, y): ...
def egypt_takenouchi(x, y): ...
def egypt_golomb(x, y): ...
def egypt_harmonic(r): ...
