def hypot(a, b):
    """
    Return the hypotenuse of a right triangle.

    >>> hypot(3, 4)
    5
    >>> hypot(5, 12)
    13
    >>> hypot(-3, -4)
    5
    """
    return (a**2 + b**2) ** 0.5
