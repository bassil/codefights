"""
"""

def countSumOfTwoRepresentations2(n, l, r):
    """
    return the number of ways to represent n as A + B for l <= A <= B <= r
    
    >>> countSumOfTwoRepresentations2(10, 9, 11)
    0

    >>> countSumOfTwoRepresentations2(93, 24, 58)
    12

    """
    count = 0
    while n-l <= r:
        if r >= l:
            pass

    return count

print(countSumOfTwoRepresentations2(93, 24, 58))

if __name__ == '__main__':
    import doctest
    # doctest.testmod(verbose=True)