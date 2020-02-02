def getPoints(answers, p):
    """
    return the number of points received based on the given list answers
    for the ith question, get i points or lose p points
    ----------
    parameters
    ----------
    answers:        list of booleans - answers to true/false questions
    p:              integer values of points lost for wrong answer
    ----------
    >>> getPoints([True, True, False, True], 2)
    5
    """
    questionPoints = lambda i, ans: i+1 if answers[i] else -p

    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)