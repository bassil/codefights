def twoTeams(students):
    """
    return the difference of the sum of the odd elements of the input list and
    the even elements of the input list
    -----------
    Parameters:
    -----------
    students:   list of integers
    -----------
    >>> twoTeams([1, 11, 13, 6, 14])
    11
    >>> twoTeams([3, 4])
    -1
    """
    return sum(students[::2]) - sum(students[1::2])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)