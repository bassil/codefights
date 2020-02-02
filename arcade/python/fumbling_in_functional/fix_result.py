def fix(x):
    """
    return x with the last digit dropped
    ----------
    parameters
    ----------
    x:      integer
    ----------
    >>> fix(142)
    14
    """
    return x // 10

def fixResult(result):
    """
    return result with fix applied on each element
    ----------
    parameters
    ----------
    result:     list of integers
    >>> fixResult([42, 239, 365, 50])
    [4, 23, 36, 5]
    """
    return list(map(fix, result))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)