from collections import Counter

def frequencyAnalysis(encryptedText):
    """returns plaintext of encryptedText

    Args:

    encryptedText - string

    Example Usage:

    >>> frequencyAnalysis("$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ")
    'C'
    """
    return Counter(encryptedText).most_common(1)[0][0]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)