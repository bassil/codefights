import functools

def mathPractice(numbers):
	"""return (((...(a[0] + a[1]) * a[2] + a[3]) * a[4] + ...),
		where a = numbers

	Args:

	numbers - list[int]
		list of numbers to perform calculation

	Example Usage:

	>>> mathPractice([1, 2, 3, 4, 5, 6])
	71

	>>> mathPractice([8, 9])
	17
	"""
	return functools.reduce(bug)

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True,
					optionflags=doctest.NORMALIZE_WHITESPACE)
