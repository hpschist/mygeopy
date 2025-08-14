def hypot(a, b):
    """
    Return the hypotenuse of a right triangle.

    >>> hypot(3, 4)
    5.0
    >>> hypot(5, 12)
    13.0
    >>> hypot(-3, -4)
    5.0
    """
    return (a**2 + b**2) ** 0.5
