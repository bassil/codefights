import functools
import itertools

def prefSum(a):
	"""return list of prefix sums

	Args:

	a - list[int]
		list of integers

	Example Usage:

	>>> prefSum([1, 2, 3])
	[1, 3, 6]

	>>> prefSum([1, 2, 3, -6])
	[1, 3, 6, 0]
	"""
	# return [sum(a[: i + 1]) for i in range(len(a))]
	# return functools.reduce(lambda p, x: p + [p[-1] + x], a, [0])[1:]
	return list(itertools.accumulate(a))

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True,
					optionflags=doctest.NORMALIZE_WHITESPACE)