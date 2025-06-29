from _typeshed import Incomplete

__all__ = ['Qasm']

class Qasm:
    defs: Incomplete
    circuit: Incomplete
    labels: Incomplete
    inits: Incomplete
    kwargs: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def add(self, *lines) -> None: ...
    def get_circuit(self): ...
    def get_labels(self): ...
    def plot(self) -> None: ...
    def qubit(self, arg, init: Incomplete | None = None) -> None: ...
    def indices(self, args): ...
    def index(self, arg): ...
    def nop(self, *args) -> None: ...
    def x(self, arg) -> None: ...
    def z(self, arg) -> None: ...
    def h(self, arg) -> None: ...
    def s(self, arg) -> None: ...
    def t(self, arg) -> None: ...
    def measure(self, arg) -> None: ...
    def cnot(self, a1, a2) -> None: ...
    def swap(self, a1, a2) -> None: ...
    def cphase(self, a1, a2) -> None: ...
    def toffoli(self, a1, a2, a3) -> None: ...
    def cx(self, a1, a2) -> None: ...
    def cz(self, a1, a2) -> None: ...
    def defbox(self, *args) -> None: ...
    def qdef(self, name, ncontrols, symbol) -> None: ...
