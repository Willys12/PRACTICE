def my_function(a, b):
    """
    >>> my_function(3, 4)
    7
    >>> my_function('g', 3)
    'g3'
    """
    if isinstance(a, str):
        b = str(b)
    return a + b