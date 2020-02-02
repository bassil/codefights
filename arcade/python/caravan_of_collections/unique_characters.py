def uniqueCharacters(document):
    """Finds and sorts the unique characters in a document.
    
    Args:
        document: A string of English letters, whitespace, and punctuation.

    Returns:
        A list of characters sorted by ascii code.

    Example usage:
        >>> uniqueCharacters("Todd told Tom to trot to the timber")
        [' ',
         'T',
         'b',
         'd',
         'e',
         'h',
         'i',
         'l',
         'm',
         'o',
         'r',
         't']
    """
    return sorted(list(set(document)))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)