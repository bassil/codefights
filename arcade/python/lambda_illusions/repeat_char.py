def repeatChar(ch, n):
    """
    return string of character ch repeated n times
    ----------
    parameters
    ----------
    ch:     character
    n:      integer
    ----------
    >>> repeatChar('*', 20)
    '********************'
    """
    repeat_char = lambda ch, n: ch*n
    return repeat_char(ch, n)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)