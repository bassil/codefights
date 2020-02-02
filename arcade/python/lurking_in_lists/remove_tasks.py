def removeTasks(k, toDo):
    """
    remove each kth task from input list toDo
    ----------
    parameters
    ----------
    k:      integer
    toDo:   list of integers
    ----------
    >>> removeTasks(3, [1237, 2847, 27485, 2947, 1, 247, 374827, 22])
    [1237, 2847, 2947, 1, 374827, 22]
    """
    del toDo[k-1::k]
    return toDo

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)