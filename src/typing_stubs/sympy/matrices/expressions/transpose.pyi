from sympy.assumptions.ask import Q as Q, ask as ask
from sympy.assumptions.refine import handlers_dict as handlers_dict
from sympy.core.basic import Basic as Basic
from sympy.matrices.expressions.matexpr import MatrixExpr as MatrixExpr

class Transpose(MatrixExpr):
    is_Transpose: bool
    def doit(self, **hints): ...
    @property
    def arg(self): ...
    @property
    def shape(self): ...

def transpose(expr): ...
def refine_Transpose(expr, assumptions): ...
