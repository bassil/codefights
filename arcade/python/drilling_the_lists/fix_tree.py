def fixTree(tree):
	"""return list of asterisk strings with each asterisk string centered
		e.g., equal whitespace on either side of asterisks

	Args:
	
	tree - list[string]
		list of misaligned asterisk strings

	Example Usage:

	# >>> fixTree(['      *  ',
	# 			 '    *    ',
	# 			 '***      ',
	# 			 '    *****',
	# 			 '  *******',
	# 			 '*********',
	# 			 ' ***     '])

	# ['    *    ',
	#  '    *    ',
	#  '   ***   ',
	#  '  *****  ',
	#  ' ******* ',
	#  '*********',
	#  '   ***   ']

	# >>> fixTree(['    *    ',
	# 			 '    *    ',
	# 			 '   ***   ',
	# 			 '  *****  ',
	# 			 ' ******* ',
	# 			 '*********',
	# 			 '   ***   '])
				 
	# ['    *    ',
	#  '    *    ',
	#  '   ***   ',
	#  '  *****  ',
	#  ' ******* ',
	#  '*********',
	#  '   ***   ']
	"""
	return [_.strip().center(len(_)) for _ in tree]

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True,
					optionflags=doctest.NORMALIZE_WHITESPACE)