from collections import deque

def doodledPassword(digits):
    """All possible combinations of digits sorted by digit index
    
    Args:

    digits - list[int]

    Example Usage:

    >>> doodledPassword([1, 2, 3, 4, 5])
    [[1, 2, 3, 4, 5],
     [2, 3, 4, 5, 1],
     [3, 4, 5, 1, 2],
     [4, 5, 1, 2, 3],
     [5, 1, 2, 3, 4]]
    """

    n = len(digits)
    res = [deque(digits) for _ in range(n)]

    deque(map(lambda x, y: x.rotate(-y), res, range(n)), 0)
    return [list(d) for d in res]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)