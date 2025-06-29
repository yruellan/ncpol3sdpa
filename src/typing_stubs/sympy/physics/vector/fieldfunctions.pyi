__all__ = ['curl', 'divergence', 'gradient', 'is_conservative', 'is_solenoidal', 'scalar_potential', 'scalar_potential_difference']

def curl(vect, frame): ...
def divergence(vect, frame): ...
def gradient(scalar, frame): ...
def is_conservative(field): ...
def is_solenoidal(field): ...
def scalar_potential(field, frame): ...
def scalar_potential_difference(field, frame, point1, point2, origin): ...
