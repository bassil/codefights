from itertools import chain, dropwhile, repeat

def memoryPills(pills):
    """return list of three strings after first even length string

    Args:

    pills - list[string]    

    Example Usage:

    >>> memoryPills(["Notforgetan", \
                     "Antimoron", \
                     "Rememberin", \
                     "Bestmedicen", \
                     "Superpillsus"])
    ['Bestmedicen', 
     'Superpillsus', 
     '']

    >>> memoryPills(["Pillin"])
    ['', '', '']
    """
    gen = chain.from_iterable([dropwhile(lambda x: len(x) % 2 != 0, pills), 
                               repeat('', 3)])
    next(gen)
    return [next(gen) for _ in range(3)]

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)