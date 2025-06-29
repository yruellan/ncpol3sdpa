import sympy
from _typeshed import Incomplete
from lark import Transformer
from sympy.external import import_module as import_module
from sympy.parsing.latex.errors import LaTeXParsingError as LaTeXParsingError

lark: Incomplete

class Transformer:
    def transform(self, *args) -> None: ...

class Token: ...

class TransformToSymPyExpr(Transformer):
    SYMBOL = sympy.Symbol
    DIGIT = sympy.core.numbers.Integer
    def CMD_INFTY(self, tokens): ...
    def GREEK_SYMBOL(self, tokens): ...
    def BASIC_SUBSCRIPTED_SYMBOL(self, tokens): ...
    def GREEK_SUBSCRIPTED_SYMBOL(self, tokens): ...
    def SYMBOL_WITH_GREEK_SUBSCRIPT(self, tokens): ...
    def multi_letter_symbol(self, tokens): ...
    def number(self, tokens): ...
    def latex_string(self, tokens): ...
    def group_round_parentheses(self, tokens): ...
    def group_square_brackets(self, tokens): ...
    def group_curly_parentheses(self, tokens): ...
    def eq(self, tokens): ...
    def ne(self, tokens): ...
    def lt(self, tokens): ...
    def lte(self, tokens): ...
    def gt(self, tokens): ...
    def gte(self, tokens): ...
    def add(self, tokens): ...
    def sub(self, tokens): ...
    def mul(self, tokens): ...
    def div(self, tokens): ...
    def adjacent_expressions(self, tokens): ...
    def superscript(self, tokens): ...
    def fraction(self, tokens): ...
    def binomial(self, tokens): ...
    def normal_integral(self, tokens): ...
    def group_curly_parentheses_int(self, tokens): ...
    def special_fraction(self, tokens): ...
    def integral_with_special_fraction(self, tokens): ...
    def group_curly_parentheses_special(self, tokens): ...
    def summation(self, tokens): ...
    def product(self, tokens): ...
    def limit_dir_expr(self, tokens): ...
    def group_curly_parentheses_lim(self, tokens): ...
    def limit(self, tokens): ...
    def differential(self, tokens): ...
    def derivative(self, tokens): ...
    def list_of_expressions(self, tokens): ...
    def function_applied(self, tokens): ...
    def min(self, tokens): ...
    def max(self, tokens): ...
    def bra(self, tokens): ...
    def ket(self, tokens): ...
    def inner_product(self, tokens): ...
    def sin(self, tokens): ...
    def cos(self, tokens): ...
    def tan(self, tokens): ...
    def csc(self, tokens): ...
    def sec(self, tokens): ...
    def cot(self, tokens): ...
    def sin_power(self, tokens): ...
    def cos_power(self, tokens): ...
    def tan_power(self, tokens): ...
    def csc_power(self, tokens): ...
    def sec_power(self, tokens): ...
    def cot_power(self, tokens): ...
    def arcsin(self, tokens): ...
    def arccos(self, tokens): ...
    def arctan(self, tokens): ...
    def arccsc(self, tokens): ...
    def arcsec(self, tokens): ...
    def arccot(self, tokens): ...
    def sinh(self, tokens): ...
    def cosh(self, tokens): ...
    def tanh(self, tokens): ...
    def asinh(self, tokens): ...
    def acosh(self, tokens): ...
    def atanh(self, tokens): ...
    def abs(self, tokens): ...
    def floor(self, tokens): ...
    def ceil(self, tokens): ...
    def factorial(self, tokens): ...
    def conjugate(self, tokens): ...
    def square_root(self, tokens): ...
    def exponential(self, tokens): ...
    def log(self, tokens): ...
