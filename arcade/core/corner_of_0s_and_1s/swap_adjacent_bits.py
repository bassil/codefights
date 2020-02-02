def swapAdjacentBits(n):
    """
    Return a base-10 integer of a 32-bit integer n
    after swapping adjacent bits in the base-2 representation of n 
    """
    binary_n = bin(n)[2:]

    # want even number of digits in binary_n
    if len(binary_n) % 2 != 0:
    	binary_n = '0'+binary_n
 	
 	# swap digits in digit pairs
    digit_pairs = [[binary_n[i+1], binary_n[i]] \
    	for i in range(0, len(binary_n), 2)]

    # join the digit pairs and convert to base-10 integer
    base_10_n = int("".join([digit for digit_pair in digit_pairs \
    	for digit in digit_pair]), 2)

    return base_10_n
##############################################################################
def swapAdjacentBits2(n):
	return ((n & 0xAAAAAAAA) >> 1 | (n & 0x55555555) << 1)
##############################################################################
# EXAMPLES

# n = 74

# print(swapAdjacentBits(n))
# print(swapAdjacentBits2(n))


