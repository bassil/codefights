from fractions import gcd
import functools

def leastCommonDenominator(denominators):
    """
    return the least common denominator of a list of denominators
    ----------
    parameters
    ----------
    denominators:       list of denominator integers
    ----------
    >>> leastCommonDenominator([2, 3, 4, 5, 6])
    60
    """    
    return functools.reduce((lambda x, y: (x * y)//gcd(x, y)), denominators)


    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)