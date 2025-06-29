from _typeshed import Incomplete
from sympy.core import Basic as Basic, Dict as Dict, Tuple as Tuple
from sympy.core.cache import cacheit as cacheit
from sympy.core.numbers import Integer as Integer
from sympy.matrices.dense import DenseMatrix as DenseMatrix
from sympy.matrices.expressions import MatrixExpr as MatrixExpr
from sympy.matrices.matrixbase import MatrixBase as MatrixBase
from sympy.matrices.repmatrix import RepMatrix as RepMatrix
from sympy.matrices.sparse import SparseRepMatrix as SparseRepMatrix
from sympy.multipledispatch import dispatch as dispatch

def sympify_matrix(arg): ...
def sympify_mpmath_matrix(arg): ...

class ImmutableRepMatrix(RepMatrix, MatrixExpr):
    def __new__(cls, *args, **kwargs): ...
    __hash__: Incomplete
    def copy(self): ...
    @property
    def cols(self): ...
    @property
    def rows(self): ...
    @property
    def shape(self): ...
    def as_immutable(self): ...
    def __setitem__(self, *args) -> None: ...
    def is_diagonalizable(self, reals_only: bool = False, **kwargs): ...
    is_diagonalizable: Incomplete
    def analytic_func(self, f, x): ...

class ImmutableDenseMatrix(DenseMatrix, ImmutableRepMatrix): ...
ImmutableMatrix = ImmutableDenseMatrix

class ImmutableSparseMatrix(SparseRepMatrix, ImmutableRepMatrix):
    is_Matrix: bool
