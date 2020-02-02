def coolPairs(a, b):
    """
    return the number of different sums of elements in cool pairs
    a pair of numbers is cool if their product is divisible by their sum
    e.g., (i, j) cool iff (i * j) % (i + j) == 0
    ----------
    parameters
    ----------
    a:      list of distinct integers
    b:      list of distinct integers
    ----------
    >>> coolPairs([4, 5, 6, 7, 8], [8, 9, 10, 11, 12])
    2
    """

    uniqueSums = {i + j for i in a for j in b if ((i * j) % (i + j) == 0)}
    return len(uniqueSums)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
