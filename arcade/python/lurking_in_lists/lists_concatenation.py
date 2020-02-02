def listsConcatenation(lst1, lst2):
    """
    Return a list of the elements in lst1 followed by the elements in lst2
    -----------
    Parameters:
    -----------
    lst1 - list
    lst2 - list
    -----------
    >>> listsConcatenation([2, 2, 1], [10, 11])
    [2, 2, 1, 10, 11]
    """
    res = lst1
    res.extend(lst2)
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)