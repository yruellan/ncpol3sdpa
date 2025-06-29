from _typeshed import Incomplete
from sympy.core.random import uniform as uniform
from sympy.external.gmpy import MPZ as MPZ, SYMPY_INTS as SYMPY_INTS, invert as invert
from sympy.polys.polyconfig import query as query
from sympy.polys.polyerrors import ExactQuotientFailed as ExactQuotientFailed

def gf_crt(U, M, K: Incomplete | None = None): ...
def gf_crt1(M, K): ...
def gf_crt2(U, M, p, E, S, K): ...
def gf_int(a, p): ...
def gf_degree(f): ...
def gf_LC(f, K): ...
def gf_TC(f, K): ...
def gf_strip(f): ...
def gf_trunc(f, p): ...
def gf_normal(f, p, K): ...
def gf_from_dict(f, p, K): ...
def gf_to_dict(f, p, symmetric: bool = True): ...
def gf_from_int_poly(f, p): ...
def gf_to_int_poly(f, p, symmetric: bool = True): ...
def gf_neg(f, p, K): ...
def gf_add_ground(f, a, p, K): ...
def gf_sub_ground(f, a, p, K): ...
def gf_mul_ground(f, a, p, K): ...
def gf_quo_ground(f, a, p, K): ...
def gf_add(f, g, p, K): ...
def gf_sub(f, g, p, K): ...
def gf_mul(f, g, p, K): ...
def gf_sqr(f, p, K): ...
def gf_add_mul(f, g, h, p, K): ...
def gf_sub_mul(f, g, h, p, K): ...
def gf_expand(F, p, K): ...
def gf_div(f, g, p, K): ...
def gf_rem(f, g, p, K): ...
def gf_quo(f, g, p, K): ...
def gf_exquo(f, g, p, K): ...
def gf_lshift(f, n, K): ...
def gf_rshift(f, n, K): ...
def gf_pow(f, n, p, K): ...
def gf_frobenius_monomial_base(g, p, K): ...
def gf_frobenius_map(f, g, b, p, K): ...
def gf_pow_mod(f, n, g, p, K): ...
def gf_gcd(f, g, p, K): ...
def gf_lcm(f, g, p, K): ...
def gf_cofactors(f, g, p, K): ...
def gf_gcdex(f, g, p, K): ...
def gf_monic(f, p, K): ...
def gf_diff(f, p, K): ...
def gf_eval(f, a, p, K): ...
def gf_multi_eval(f, A, p, K): ...
def gf_compose(f, g, p, K): ...
def gf_compose_mod(g, h, f, p, K): ...
def gf_trace_map(a, b, c, n, f, p, K): ...
def gf_random(n, p, K): ...
def gf_irreducible(n, p, K): ...
def gf_irred_p_ben_or(f, p, K): ...
def gf_irred_p_rabin(f, p, K): ...
def gf_irreducible_p(f, p, K): ...
def gf_sqf_p(f, p, K): ...
def gf_sqf_part(f, p, K): ...
def gf_sqf_list(f, p, K, all: bool = False): ...
def gf_Qmatrix(f, p, K): ...
def gf_Qbasis(Q, p, K): ...
def gf_berlekamp(f, p, K): ...
def gf_ddf_zassenhaus(f, p, K): ...
def gf_edf_zassenhaus(f, n, p, K): ...
def gf_ddf_shoup(f, p, K): ...
def gf_edf_shoup(f, n, p, K): ...
def gf_zassenhaus(f, p, K): ...
def gf_shoup(f, p, K): ...
def gf_factor_sqf(f, p, K, method: Incomplete | None = None): ...
def gf_factor(f, p, K): ...
def gf_value(f, a): ...
def linear_congruence(a, b, m): ...
def csolve_prime(f, p, e: int = 1): ...
def gf_csolve(f, n): ...
