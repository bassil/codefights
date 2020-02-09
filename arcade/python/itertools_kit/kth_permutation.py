from itertools import permutations, dropwhile

def kthPermutation(numbers, k):
    """return kth permutation of list of numbers

    Args:

    numbers - list[int]
        sorted list of distinct ints
    k - int
        1-based index of the return permutation

    Example Usage:

    >>> kthPermutation([1, 2, 3, 4, 5], 4)
    [1, 2, 4, 5, 3]
    >>> kthPermutation([1, 2], 1)
    [1, 2]
    """
    gen = permutations(numbers)
    return [next(gen) for _ in range(k)].last()

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)