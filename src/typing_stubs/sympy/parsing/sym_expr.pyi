from _typeshed import Incomplete
from sympy.external import import_module as import_module
from sympy.parsing.c.c_parser import parse_c as parse_c
from sympy.parsing.fortran.fortran_parser import src_to_sympy as src_to_sympy
from sympy.printing import ccode as ccode, fcode as fcode, pycode as pycode
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on

lfortran: Incomplete
cin: Incomplete

class SymPyExpression:
    def __init__(self, source_code: Incomplete | None = None, mode: Incomplete | None = None) -> None: ...
    def convert_to_expr(self, src_code, mode) -> None: ...
    def convert_to_python(self): ...
    def convert_to_c(self): ...
    def convert_to_fortran(self): ...
    def return_expr(self): ...
