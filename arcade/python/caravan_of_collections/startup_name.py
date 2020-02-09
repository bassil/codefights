def startupName(companies):
    """return sorted list of characters that are popular but not mainstream

    A popular character appears in at least two company names.
    A mainstream character appears in three company names.

    Args:

    companies - List of three strings - [string, string, string]
        The strings represent company names and are lowercase

    Examples:

    >>> startupName(["coolcompany", "nicecompany", "legendarycompany"])
    ['e', 'l']

    >>> startupName(["nameone", "nametwo", "namethree"])
    ['o', 't']
    """
    cmp1 = set(companies[0])
    cmp2 = set(companies[1])
    cmp3 = set(companies[2])
    
    res = cmp1.intersection(cmp2).\
               difference(cmp3).\
               union(cmp1.intersection(cmp3).\
                          difference(cmp2), 
                     cmp2.intersection(cmp3).\
                          difference(cmp1))

    return list(sorted(list(res)))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
