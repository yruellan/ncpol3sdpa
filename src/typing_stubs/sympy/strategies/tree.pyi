from sympy.strategies import chain as chain, minimize as minimize
from sympy.strategies.branch import yieldify as yieldify
from sympy.strategies.core import identity as identity

def treeapply(tree, join, leaf=...): ...
def greedy(tree, objective=..., **kwargs): ...
def allresults(tree, leaf=...): ...
def brute(tree, objective=..., **kwargs): ...
