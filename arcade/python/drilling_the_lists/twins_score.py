def twinsScore(b, m):
	""" return a list of the piecewise sums of b and m

	Args:

	b - list[int]
		list of Billy's test scores
	m - list[int]
		list of Mandy's test scores

	Example Usage:

	>>> twinsScore([22, 13, 45, 32], [28, 41, 13, 32])
	[50, 54, 58, 64]
	>>> twinsScore([0, 0, 0], [100, 100, 100])
	[100, 100, 100]
	"""
	return list(map(lambda x, y: x + y, b, m))

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True,
					optionflags=doctest.NORMALIZE_WHITESPACE)
