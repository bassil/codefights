from itertools import count, takewhile

def floatRange(start, stop, step):
    """returns a list of floats between start and stop evenly spaced by step
    
    NOTE - The behavior of this implementation is correct,
    but the doctests WILL FAIL because of floating point precision. 
    I will explore this topic in the future (although, pragmatically,
    I probably won't revise this exact function)

    Args:

    start - float
        lower bound of float range list (included in float range)
    stop - float
        upper bound of float range list (not included in float range)
    step - float
        size of step between elements of float range

    Example Usage:

    >>> floatRange(1, 2, 0.1)
    [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]

    >>> floatRange(-0.9, 0.45, 0.2)
    [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3]
    """
    gen = takewhile(lambda x: x < stop, count(start, step))
    return list(gen)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)