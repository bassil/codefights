def groupDating(male, female):
    """return list of indexes of male and female cats without same nature value

	Args:

	male - list[int]
		list of nature values of male cats
	female - list[int]
		list of nature values of female cats

	Example Usage:

	>>> groupDating([5, 28, 14, 99, 17], [5, 14, 28, 99, 16])
	[[28, 14, 17],
	 [14, 28, 16]]
	>>> groupDating([42], [64])
	[[42],
	 [64]]
    """
    return [[i for i, j in zip(male, female) if i != j],
    		[j for i, j in zip(male, female) if i != j]]

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True,
					optionflags=doctest.NORMALIZE_WHITESPACE)