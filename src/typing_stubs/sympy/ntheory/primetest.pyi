from _typeshed import Incomplete
from sympy.core.sympify import sympify as sympify
from sympy.external.gmpy import bit_scan1 as bit_scan1, gcd as gcd, is_euler_prp as is_euler_prp, is_fermat_prp as is_fermat_prp, is_selfridge_prp as is_selfridge_prp, is_strong_bpsw_prp as is_strong_bpsw_prp, is_strong_selfridge_prp as is_strong_selfridge_prp, jacobi as jacobi
from sympy.utilities.misc import as_int as as_int, filldedent as filldedent

MERSENNE_PRIME_EXPONENTS: Incomplete

def is_fermat_pseudoprime(n, a): ...
def is_euler_pseudoprime(n, a): ...
def is_euler_jacobi_pseudoprime(n, a): ...
def is_square(n, prep: bool = True): ...
def mr(n, bases): ...
def is_lucas_prp(n): ...
def is_strong_lucas_prp(n): ...
def is_extra_strong_lucas_prp(n): ...
def proth_test(n): ...
def is_mersenne_prime(n): ...
def isprime(n): ...
def is_gaussian_prime(num): ...
