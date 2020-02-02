def isTestSolvable(ids, k):
    """
    return 
    ----------
    parameters
    ----------
    >>> isTestSolvable([529665, 909767, 644200], 3)
    True
    """
    digitSum = lambda x: sum([int(digit) for digit in str(x)])

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)