def correctLineup(athletes):
	"""return athletes list with adjacent pairs swapped,
		e.g., [0, 1, 2, 3] --> [1, 0, 3, 2]

	Args:

	athletes - list[int]
		A 'correct' lineup of boy and girl athletes (no adjacent boys or girls)

	Example Usage:

	>>> correctLineup([1, 2, 3, 4, 5, 6])
	[2, 1, 4, 3, 6, 5]
	
	>>> correctLineup([13, 42])
	[42, 13]
	"""
	return [item for sublist in [[athletes[i+1], athletes[i]] for i in range(len(athletes)) if i % 2 == 0] for item in sublist]

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True,
					optionflags=doctest.NORMALIZE_WHITESPACE)