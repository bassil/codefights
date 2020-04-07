# from itertools import 

def crackingPassword(digits, k, d):
	"""return list of possible passwords

	Args:

	digits - list[int]
		list of possible elements of password
	k - int
		length of password
	d - int
		divisor of password

    Example Usage:

	>>> crackingPassword([1, 5, 2], 2, 3)
	['12',
	 '15',
	 '21',
	 '51']
	>>> crackingPassword([4, 6, 0, 3], 4, 13)
	['0000',
	 '0364',
	 '0403',
	 '0663',
	 '3003',
	 '3406',
	 '3640',
	 '3666',
	 '4004',
	 '4030',
	 '4043',
	 '4303',
	 '4433',
	 '4446',
	 '6006',
	 '6344',
	 '6604',
	 '6630',
	 '6643']
	"""
	def createNumber(digs):
		return "".join(map(str, digs))

	return 

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True,
					optionflags=doctest.NORMALIZE_WHITESPACE)