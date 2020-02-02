def printList(lst):
    """
    return the string "This is your list: [list_1, list_2, ...]"
    >>> printList([1, 2, 3, 4, 5])
    'This is your list: [1, 2, 3, 4, 5]'
    """
    return "This is your list: {}".format(lst)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)