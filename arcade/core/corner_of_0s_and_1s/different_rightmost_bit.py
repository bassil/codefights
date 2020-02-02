def differentRightmostBit(n, m):
    """
    return the 2^(position) of the rightmost bit in which n and m differ

    >>> differentRightmostBit(11, 13)
    2
    
    >>> differentRightmostBit(7, 23)
    16

    >>> differentRightmostBit(1073741823, 1071513599)
    131072
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
        if binary_n[binary_index] != binary_m[binary_index]:
            break
        position_from_right+=1

    return 2**position_from_right

# print(differentRightmostBit(7, 23))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    