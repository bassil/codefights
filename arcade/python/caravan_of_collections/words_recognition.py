def wordsRecognition(word1, word2):
    """return sorted list of a first word and a second word
    
    given word1 and word2, return a list of two lexicographically
    sorted strings such that the first string contains characters
    present only in word1 and the second string contains characters
    present only in word2.
    Args:

    word1 - string - lowercase
    word2 - string - lowercase

    Examples:

    >>> wordsRecognition("program", "develop")
    ['agmr', 'delv']

    >>> wordsRecognition("code", "fights")
    ['cdeo', 'fghist']
    """
    def getIdentifier(w1, w2):
        """returns characters in w1 but not w2"""
        return "".join(sorted(list(set(w1).difference(set(w2)))))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)