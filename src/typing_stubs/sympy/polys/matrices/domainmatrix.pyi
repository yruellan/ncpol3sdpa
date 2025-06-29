from ..constructor import construct_domain as construct_domain
from ..domains import Domain as Domain
from .ddm import DDM as DDM
from .dfm import DFM as DFM
from .domainscalar import DomainScalar as DomainScalar
from .exceptions import DMBadInputError as DMBadInputError, DMDomainError as DMDomainError, DMFormatError as DMFormatError, DMNonInvertibleMatrixError as DMNonInvertibleMatrixError, DMNonSquareMatrixError as DMNonSquareMatrixError, DMNotAField as DMNotAField, DMShapeError as DMShapeError
from .sdm import SDM as SDM
from _typeshed import Incomplete
from sympy.external.gmpy import GROUND_TYPES as GROUND_TYPES
from sympy.polys.densearith import dup_mul as dup_mul
from sympy.polys.densebasic import dup_convert as dup_convert
from sympy.polys.densetools import dup_clear_denoms as dup_clear_denoms, dup_content as dup_content, dup_mul_ground as dup_mul_ground, dup_primitive as dup_primitive, dup_quo_ground as dup_quo_ground, dup_transform as dup_transform
from sympy.polys.domains import EXRAW as EXRAW, QQ as QQ, ZZ as ZZ
from sympy.polys.factortools import dup_factor_list as dup_factor_list
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on

__doctest_skip__: Incomplete

def DM(rows, domain): ...

class DomainMatrix:
    rep: SDM | DDM | DFM
    shape: tuple[int, int]
    domain: Domain
    def __new__(cls, rows, shape, domain, *, fmt: Incomplete | None = None): ...
    def __reduce__(self): ...
    def __getitem__(self, key): ...
    def getitem_sympy(self, i, j): ...
    def extract(self, rowslist, colslist): ...
    def __setitem__(self, key, value) -> None: ...
    @classmethod
    def from_rep(cls, rep): ...
    @classmethod
    def from_list(cls, rows, domain): ...
    @classmethod
    def from_list_sympy(cls, nrows, ncols, rows, **kwargs): ...
    @classmethod
    def from_dict_sympy(cls, nrows, ncols, elemsdict, **kwargs): ...
    @classmethod
    def from_Matrix(cls, M, fmt: str = 'sparse', **kwargs): ...
    @classmethod
    def get_domain(cls, items_sympy, **kwargs): ...
    def choose_domain(self, **opts): ...
    def copy(self): ...
    def convert_to(self, K): ...
    def to_sympy(self): ...
    def to_field(self): ...
    def to_sparse(self): ...
    def to_dense(self): ...
    def to_ddm(self): ...
    def to_sdm(self): ...
    def to_dfm(self): ...
    def to_dfm_or_ddm(self): ...
    def unify(self, *others, fmt: Incomplete | None = None): ...
    def to_Matrix(self): ...
    def to_list(self): ...
    def to_list_flat(self): ...
    @classmethod
    def from_list_flat(cls, elements, shape, domain): ...
    def to_flat_nz(self): ...
    def from_flat_nz(self, elements, data, domain): ...
    def to_dod(self): ...
    @classmethod
    def from_dod(cls, dod, shape, domain): ...
    def from_dod_like(self, dod, domain: Incomplete | None = None): ...
    def to_dok(self): ...
    @classmethod
    def from_dok(cls, dok, shape, domain): ...
    def iter_values(self): ...
    def iter_items(self): ...
    def nnz(self): ...
    def transpose(self): ...
    def flat(self): ...
    @property
    def is_zero_matrix(self): ...
    @property
    def is_upper(self): ...
    @property
    def is_lower(self): ...
    @property
    def is_diagonal(self): ...
    def diagonal(self): ...
    @property
    def is_square(self): ...
    def rank(self): ...
    def hstack(A, *B): ...
    def vstack(A, *B): ...
    def applyfunc(self, func, domain: Incomplete | None = None): ...
    def __add__(A, B): ...
    def __sub__(A, B): ...
    def __neg__(A): ...
    def __mul__(A, B): ...
    def __rmul__(A, B): ...
    def __pow__(A, n): ...
    def add(A, B): ...
    def sub(A, B): ...
    def neg(A): ...
    def mul(A, b): ...
    def rmul(A, b): ...
    def matmul(A, B): ...
    def scalarmul(A, lamda): ...
    def rscalarmul(A, lamda): ...
    def mul_elementwise(A, B): ...
    def __truediv__(A, lamda): ...
    def pow(A, n): ...
    def scc(self): ...
    def clear_denoms(self, convert: bool = False): ...
    def clear_denoms_rowwise(self, convert: bool = False): ...
    def cancel_denom(self, denom): ...
    def cancel_denom_elementwise(self, denom): ...
    def content(self): ...
    def primitive(self): ...
    def rref(self, *, method: str = 'auto'): ...
    def rref_den(self, *, method: str = 'auto', keep_domain: bool = True): ...
    def columnspace(self): ...
    def rowspace(self): ...
    def nullspace(self, divide_last: bool = False): ...
    def nullspace_from_rref(self, pivots: Incomplete | None = None): ...
    def inv(self): ...
    def det(self): ...
    def adj_det(self): ...
    def adjugate(self): ...
    def inv_den(self, method: Incomplete | None = None): ...
    def solve_den(self, b, method: Incomplete | None = None): ...
    def solve_den_rref(self, b): ...
    def solve_den_charpoly(self, b, cp: Incomplete | None = None, check: bool = True): ...
    def adj_poly_det(self, cp: Incomplete | None = None): ...
    def eval_poly(self, p): ...
    def eval_poly_mul(self, p, B): ...
    def lu(self): ...
    def lu_solve(self, rhs): ...
    def charpoly(self): ...
    def charpoly_factor_list(self): ...
    def charpoly_factor_blocks(self): ...
    def charpoly_base(self): ...
    def charpoly_berk(self): ...
    @classmethod
    def eye(cls, shape, domain): ...
    @classmethod
    def diag(cls, diagonal, domain, shape: Incomplete | None = None): ...
    @classmethod
    def zeros(cls, shape, domain, *, fmt: str = 'sparse'): ...
    @classmethod
    def ones(cls, shape, domain): ...
    def __eq__(A, B): ...
    def unify_eq(A, B): ...
    def lll(A, delta=...): ...
    def lll_transform(A, delta=...): ...
