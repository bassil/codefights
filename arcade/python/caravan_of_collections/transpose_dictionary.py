def transposeDictionary(scriptByExtension):
    """return list of [extension, script] pairs sorted by extension
    
    Args:

    scriptByExtension - dict{string: string}
    dictionary of file extension strings keyed by script name strings

    Example Usage:

    >>> transposeDictionary({"validate": "py", \
                             "getLimits": "md", \
                             "generateOutputs": "json"})
    [['json', 'generateOutputs'], 
     ['md', 'getLimits'],
     ['py', 'validate']]

    >>> transposeDictionary({"styleChecker": "cp",\
                             "autoBugfixes": "py"})
    [['cp', 'styleChecker'],
     ['py', 'autoBugfixes']]
    """
    return sorted([[extension, script] \
                   for script, extension in scriptByExtension.items()])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)