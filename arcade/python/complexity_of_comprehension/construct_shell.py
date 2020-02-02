def constructShell(n):
    """
    return a shell - a 2D list of size 2*n-1 with a special configuration
    ----------
    parameters
    ----------
    n:      integer
    ----------
    >>> constructShell(3)
    [[0], [0, 0], [0, 0, 0], [0, 0], [0]]
    """
    return [[0]*(i+1) for i in range(n)] + [[0]*(i+1) for i in range(n-2, -1, -1)]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
