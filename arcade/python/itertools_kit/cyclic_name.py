from itertools import cycle

def cyclicName(name, n):
    """return cyclic string with n chars consisting of chars from name

    Args:

    name - string - cyclic prefix
    n - int - length of returned string

    Example Usage:

    >>> cyclicName('nicecoder', 15)
    'nicecoderniceco'
    >>> cyclicName('codesignal', 50)
    'codesignalcodesignalcodesignalcodesignalcodesignal'
    """
    gen = cycle(name)
    res = [next(gen) for _ in range(n)]
    return ''.join(res)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)