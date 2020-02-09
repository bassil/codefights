from itertools import permutations

def rockPaperScissors(players):
    """return lexicographically sorted list of round robin matches between players

    Args:

    players - list[string]

    Example Usage:

    >>> rockPaperScissors(['trainee', 'warrior', 'ninja'])
    [['ninja', 'trainee'],
     ['ninja', 'warrior'],
     ['trainee', 'ninja'],
     ['trainee', 'warrior'],
     ['warrior', 'ninja'],
     ['warrior', 'trainee']]
    """
    return sorted([[p1, p2] for (p1, p2) in permutations(players, 2)])

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)