from cvxpy.atoms.affine.affine_atom import AffAtom as AffAtom

class imag(AffAtom):
    def __init__(self, expr) -> None: ...
    def numeric(self, values): ...
    def shape_from_args(self) -> tuple[int, ...]: ...
    def is_imag(self) -> bool: ...
    def is_complex(self) -> bool: ...
    def is_symmetric(self) -> bool: ...
