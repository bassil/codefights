def createHistogram(ch, assignments):
    """
    return a list representing a horizontal histogram of ch for each assignment
    ----------
    parameters
    ----------
    ch:                 character
    assignments:        list of integers
    ----------
    >>> createHistogram('*', [12, 12, 14, 3, 12, 15, 14])
    ['************',
     '************',
     '**************',
     '***',
     '************',
     '***************',
     '**************']
    """
    return list(map(lambda x: ch*x, assignments))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)