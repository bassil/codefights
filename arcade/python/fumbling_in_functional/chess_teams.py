def chessTeams(smarties, cleveries):
    """
    return the chess games in the order they will be played
    the ith member of team smarties will play against 
    the ith member of team cleveries in the ith game
    ----------
    parameters
    ----------
    smarties:       list of strings - names of players on team smarties
    cleveries:     list of strings - names of players on team cleverlies
    ----------
    >>> chessTeams(["Jane", "Bob", "Peter"], ["Oscar", "Lidia", "Ann"])
    [['Jane', 'Oscar'],
     ['Bob', 'Lidia'],
     ['Peter', 'Ann']]
    """
    return list(map(lambda x, y: [x, y], smarties, cleveries))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)