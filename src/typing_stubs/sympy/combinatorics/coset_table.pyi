from _typeshed import Incomplete
from sympy.combinatorics.free_groups import free_group as free_group
from sympy.printing.defaults import DefaultPrinting as DefaultPrinting

class CosetTable(DefaultPrinting):
    coset_table_max_limit: int
    coset_table_limit: Incomplete
    max_stack_size: int
    fp_group: Incomplete
    subgroup: Incomplete
    p: Incomplete
    A: Incomplete
    P: Incomplete
    table: Incomplete
    A_dict: Incomplete
    A_dict_inv: Incomplete
    deduction_stack: Incomplete
    p_p: Incomplete
    def __init__(self, fp_grp, subgroup, max_cosets: Incomplete | None = None) -> None: ...
    @property
    def omega(self): ...
    def copy(self): ...
    @property
    def n(self): ...
    def is_complete(self): ...
    def define(self, alpha, x, modified: bool = False) -> None: ...
    def define_c(self, alpha, x) -> None: ...
    def scan_c(self, alpha, word) -> None: ...
    def coincidence_c(self, alpha, beta) -> None: ...
    def scan(self, alpha, word, y: Incomplete | None = None, fill: bool = False, modified: bool = False) -> None: ...
    def scan_check(self, alpha, word): ...
    def merge(self, k, lamda, q, w: Incomplete | None = None, modified: bool = False) -> None: ...
    def rep(self, k, modified: bool = False): ...
    def coincidence(self, alpha, beta, w: Incomplete | None = None, modified: bool = False) -> None: ...
    def scan_and_fill(self, alpha, word) -> None: ...
    def scan_and_fill_c(self, alpha, word) -> None: ...
    def look_ahead(self) -> None: ...
    def process_deductions(self, R_c_x, R_c_x_inv) -> None: ...
    def process_deductions_check(self, R_c_x, R_c_x_inv): ...
    def switch(self, beta, gamma) -> None: ...
    def standardize(self) -> None: ...
    def compress(self) -> None: ...
    def conjugates(self, R): ...
    def coset_representative(self, coset): ...
    def modified_define(self, alpha, x) -> None: ...
    def modified_scan(self, alpha, w, y, fill: bool = False) -> None: ...
    def modified_scan_and_fill(self, alpha, w, y) -> None: ...
    def modified_merge(self, k, lamda, w, q) -> None: ...
    def modified_rep(self, k) -> None: ...
    def modified_coincidence(self, alpha, beta, w) -> None: ...

def coset_enumeration_r(fp_grp, Y, max_cosets: Incomplete | None = None, draft: Incomplete | None = None, incomplete: bool = False, modified: bool = False): ...
def modified_coset_enumeration_r(fp_grp, Y, max_cosets: Incomplete | None = None, draft: Incomplete | None = None, incomplete: bool = False): ...
def coset_enumeration_c(fp_grp, Y, max_cosets: Incomplete | None = None, draft: Incomplete | None = None, incomplete: bool = False): ...
