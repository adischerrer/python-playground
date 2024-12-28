from math import pi


def circle_area(r: int | float) -> float:
    if r < 0:
        raise ValueError('Radius cannot be negative')
    elif type(r) not in [int, float]:
        raise TypeError('Radius must be a number')
    return pi * r * r
