from _typeshed import Incomplete
from collections.abc import Generator
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.function import Function
from sympy.functions.special.tensor_functions import KroneckerDelta as KroneckerDelta
from sympy.printing.str import StrPrinter

__all__ = ['Dagger', 'KroneckerDelta', 'BosonicOperator', 'AnnihilateBoson', 'CreateBoson', 'AnnihilateFermion', 'CreateFermion', 'FockState', 'FockStateBra', 'FockStateKet', 'FockStateBosonKet', 'FockStateBosonBra', 'FockStateFermionKet', 'FockStateFermionBra', 'BBra', 'BKet', 'FBra', 'FKet', 'F', 'Fd', 'B', 'Bd', 'apply_operators', 'InnerProduct', 'BosonicBasis', 'VarBosonicBasis', 'FixedBosonicBasis', 'Commutator', 'matrix_rep', 'contraction', 'wicks', 'NO', 'evaluate_deltas', 'AntiSymmetricTensor', 'substitute_dummies', 'PermutationOperator', 'simplify_index_permutations']

class SecondQuantizationError(Exception): ...
class AppliesOnlyToSymbolicIndex(SecondQuantizationError): ...
class ContractionAppliesOnlyToFermions(SecondQuantizationError): ...
class ViolationOfPauliPrinciple(SecondQuantizationError): ...
class SubstitutionOfAmbigousOperatorFailed(SecondQuantizationError): ...
class WicksTheoremDoesNotApply(SecondQuantizationError): ...

class Dagger(Expr):
    def __new__(cls, arg): ...
    @classmethod
    def eval(cls, arg): ...

class TensorSymbol(Expr):
    is_commutative: bool

class AntiSymmetricTensor(TensorSymbol):
    def __new__(cls, symbol, upper, lower): ...
    @property
    def symbol(self): ...
    @property
    def upper(self): ...
    @property
    def lower(self): ...

class SqOperator(Expr):
    op_symbol: str
    is_commutative: bool
    def __new__(cls, k): ...
    @property
    def state(self): ...
    @property
    def is_symbolic(self): ...
    def apply_operator(self, state) -> None: ...

class BosonicOperator(SqOperator): ...
class Annihilator(SqOperator): ...
class Creator(SqOperator): ...

class AnnihilateBoson(BosonicOperator, Annihilator):
    op_symbol: str
    def apply_operator(self, state): ...

class CreateBoson(BosonicOperator, Creator):
    op_symbol: str
    def apply_operator(self, state): ...
B = AnnihilateBoson
Bd = CreateBoson

class FermionicOperator(SqOperator):
    @property
    def is_restricted(self): ...
    @property
    def is_above_fermi(self): ...
    @property
    def is_below_fermi(self): ...
    @property
    def is_only_below_fermi(self): ...
    @property
    def is_only_above_fermi(self): ...

class AnnihilateFermion(FermionicOperator, Annihilator):
    op_symbol: str
    def apply_operator(self, state): ...
    @property
    def is_q_creator(self): ...
    @property
    def is_q_annihilator(self): ...
    @property
    def is_only_q_creator(self): ...
    @property
    def is_only_q_annihilator(self): ...

class CreateFermion(FermionicOperator, Creator):
    op_symbol: str
    def apply_operator(self, state): ...
    @property
    def is_q_creator(self): ...
    @property
    def is_q_annihilator(self): ...
    @property
    def is_only_q_creator(self): ...
    @property
    def is_only_q_annihilator(self): ...
Fd = CreateFermion
F = AnnihilateFermion

class FockState(Expr):
    is_commutative: bool
    def __new__(cls, occupations): ...
    def __getitem__(self, i): ...
    def __len__(self) -> int: ...

class BosonState(FockState):
    def up(self, i): ...
    def down(self, i): ...

class FermionState(FockState):
    fermi_level: int
    def __new__(cls, occupations, fermi_level: int = 0): ...
    def up(self, i): ...
    def down(self, i): ...

class FockStateKet(FockState):
    lbracket: str
    rbracket: str
    lbracket_latex: str
    rbracket_latex: str

class FockStateBra(FockState):
    lbracket: str
    rbracket: str
    lbracket_latex: str
    rbracket_latex: str
    def __mul__(self, other): ...

class FockStateBosonKet(BosonState, FockStateKet): ...
class FockStateBosonBra(BosonState, FockStateBra): ...
class FockStateFermionKet(FermionState, FockStateKet): ...
class FockStateFermionBra(FermionState, FockStateBra): ...
BBra = FockStateBosonBra
BKet = FockStateBosonKet
FBra = FockStateFermionBra
FKet = FockStateFermionKet

def apply_operators(e): ...

class InnerProduct(Basic):
    is_commutative: bool
    def __new__(cls, bra, ket): ...
    @classmethod
    def eval(cls, bra, ket): ...
    @property
    def bra(self): ...
    @property
    def ket(self): ...

def matrix_rep(op, basis): ...

class BosonicBasis: ...

class VarBosonicBasis:
    n_max: Incomplete
    def __init__(self, n_max) -> None: ...
    def index(self, state): ...
    def state(self, i): ...
    def __getitem__(self, i): ...
    def __len__(self) -> int: ...

class FixedBosonicBasis(BosonicBasis):
    n_particles: Incomplete
    n_levels: Incomplete
    def __init__(self, n_particles, n_levels) -> None: ...
    def index(self, state): ...
    def state(self, i): ...
    def __getitem__(self, i): ...
    def __len__(self) -> int: ...

class Commutator(Function):
    is_commutative: bool
    @classmethod
    def eval(cls, a, b): ...
    def doit(self, **hints): ...

class NO(Expr):
    is_commutative: bool
    def __new__(cls, arg): ...
    @property
    def has_q_creators(self): ...
    @property
    def has_q_annihilators(self): ...
    def doit(self, **hints): ...
    def __getitem__(self, i): ...
    def __len__(self) -> int: ...
    def iter_q_annihilators(self) -> Generator[Incomplete]: ...
    def iter_q_creators(self) -> Generator[Incomplete]: ...
    def get_subNO(self, i): ...

def contraction(a, b): ...
def evaluate_deltas(e): ...
def substitute_dummies(expr, new_indices: bool = False, pretty_indices={}): ...

class KeyPrinter(StrPrinter): ...

class _SymbolFactory:
    def __init__(self, label) -> None: ...

def wicks(e, **kw_args): ...

class PermutationOperator(Expr):
    is_commutative: bool
    def __new__(cls, i, j): ...
    def get_permuted(self, expr): ...

def simplify_index_permutations(expr, permutation_operators): ...
