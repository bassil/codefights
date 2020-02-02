def wordPower(word):
    """
    return the power of a word
    the power of a word is the sum of the powers of its characters
    the power of a character is equal to its 1-based index in the alphabet
    ----------
    parameters
    ----------
    word:       a string of lowercase english letters
    >>> wordPower('hello')
    52
    """
    num = {char: power+1 for power, char in enumerate('abcdefghijklmnopqrstuvwxyz')}
    return sum([num[ch] for ch in word])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
