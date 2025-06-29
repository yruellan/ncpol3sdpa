from sympy.core.add import Add as Add
from sympy.core.containers import Tuple as Tuple
from sympy.core.function import expand as expand
from sympy.core.mul import Mul as Mul
from sympy.core.singleton import S as S
from sympy.functions.elementary.exponential import log as log
from sympy.physics.quantum.dagger import Dagger as Dagger
from sympy.physics.quantum.matrixutils import numpy_ndarray as numpy_ndarray, scipy_sparse_matrix as scipy_sparse_matrix, to_numpy as to_numpy
from sympy.physics.quantum.operator import HermitianOperator as HermitianOperator
from sympy.physics.quantum.represent import represent as represent
from sympy.physics.quantum.tensorproduct import TensorProduct as TensorProduct, tensor_product_simp as tensor_product_simp
from sympy.physics.quantum.trace import Tr as Tr
from sympy.printing.pretty.stringpict import prettyForm as prettyForm

class Density(HermitianOperator):
    def states(self): ...
    def probs(self): ...
    def get_state(self, index): ...
    def get_prob(self, index): ...
    def apply_op(self, op): ...
    def doit(self, **hints): ...
    def entropy(self): ...

def entropy(density): ...
def fidelity(state1, state2): ...
