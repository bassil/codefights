def correctScholarships(bestStudents, scholarships, allStudents):
    """Determines if scholarships are correctly distributed.

    The scholarships are considered to be correctly distributed if all of the
    best students have scholarships, not all of the students in the university
    have scholarships, and no students from outside of the university have 
    been given a scholarship.

    Args:
        bestStudents: A list of integers of the best students.
        scholarships: A list of integers of the students with scholarships.
        allStudents: A list of integers of all of the students.

    Returns:
        A boolean representing if the scholarships are correctly distributed.

    Example usage:
        >>> correctScholarships([3, 5], [3, 5, 7], [1, 2, 3, 4, 5, 6, 7])
        True
        >>> correctScholarships([3], [1, 3, 5], [1, 2, 3])
        False
        >>> correctScholarships([3, 5], [3, 5], [3, 5])
        False
    """
    return set(bestStudents).issubset(set(scholarships)) and \
           set(scholarships).issubset(set(allStudents)) and \
           set(scholarships) != set(allStudents)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)