from _typeshed import Incomplete
from sympy.combinatorics.fp_groups import FpGroup as FpGroup, FpSubgroup as FpSubgroup, simplify_presentation as simplify_presentation
from sympy.combinatorics.free_groups import FreeGroup as FreeGroup
from sympy.combinatorics.perm_groups import PermutationGroup as PermutationGroup
from sympy.core.intfunc import igcd as igcd
from sympy.core.singleton import S as S
from sympy.functions.combinatorial.numbers import totient as totient

class GroupHomomorphism:
    domain: Incomplete
    codomain: Incomplete
    images: Incomplete
    def __init__(self, domain, codomain, images) -> None: ...
    def invert(self, g): ...
    def kernel(self): ...
    def image(self): ...
    def __call__(self, elem): ...
    def is_injective(self): ...
    def is_surjective(self): ...
    def is_isomorphism(self): ...
    def is_trivial(self): ...
    def compose(self, other): ...
    def restrict_to(self, H): ...
    def invert_subgroup(self, H): ...

def homomorphism(domain, codomain, gens, images=(), check: bool = True): ...
def orbit_homomorphism(group, omega): ...
def block_homomorphism(group, blocks): ...
def group_isomorphism(G, H, isomorphism: bool = True): ...
def is_isomorphic(G, H): ...
