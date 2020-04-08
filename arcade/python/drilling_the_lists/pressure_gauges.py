def pressureGauges(morning, evening):
	"""return list of max pressure and list of min pressure
	
	Args:

	morning - list[int]
		list of morning pressure measurements
	evening - list[int]
		list of evening pressure measurements

	Example Usage:

	>>> pressureGauges([3, 5, 2, 6], [1, 6, 6, 6])
	[[1, 5, 2, 6],
	 [3, 6, 6, 6]]

	>>> pressureGauges([0, 12, 478, 23, 1000], [48, 23, 56, 23, 88])
	[[0, 12, 56, 23, 88],
	 [48, 23, 478, 23, 1000]]
	"""
	return [list(map(lambda x, y: min(x, y), morning, evening)),
			list(map(lambda x, y: max(x, y), morning, evening))]

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True,
					optionflags=doctest.NORMALIZE_WHITESPACE)