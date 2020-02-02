def multiplicationTable(n):
    """
    return the multiplication for 1 through n
    ----------
    parameters
    ----------
    n:      integer
    ----------
    >>> multiplicationTable(5)
    [[1, 2, 3, 4, 5], 
     [2, 4, 6, 8, 10],
     [3, 6, 9, 12, 15],
     [4, 8, 12, 16, 20],
     [5, 10, 15, 20, 25]]
    """
    return [[(i+1)*(j+1) for i in range(n)] for j in range(n)]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)
