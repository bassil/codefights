def equalPairOfBits(n, m):
    """
    return 2^(position) of rightmost pair of equal bits in binary reprentation
    
    >>> equalPairOfBits(10, 11)
    2

    >>> equalPairOfBits(895, 928)
    32
    
    >>> equalPairOfBits(1073741824, 1006895103)
    262144
    """
    binary_n = bin(n)[2:]
    binary_m = bin(m)[2:]

    # pad shorter binary number with 0's
    padding = "0"*(abs(len(binary_m) - len(binary_n)))

    if len(binary_m) > len(binary_n):
        binary_n = padding + binary_n
    else:
        binary_m = padding + binary_m
    
    position_from_right = 0
    
    # find the bit, starting from the right, in which n and m differ
    for binary_index in list(range(len(binary_m)-1, -1, -1)):
        if binary_n[binary_index] == binary_m[binary_index]:
            break
        position_from_right+=1

    return 2**position_from_right

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
  