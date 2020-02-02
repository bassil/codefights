def sortStudents(students):
    """
    return list of students lexicographically sorted by last name
    -----------
    parameters:
    -----------
    students:       list of student strings
    -----------
    >>> sortStudents(["John Smith", "Jacky Mon Simonoff", "Lucy Smith", "Angela Zimonova"])
    ['Jacky Mon Simonoff', 'John Smith', 'Lucy Smith', 'Angela Zimonova']
    """

    students.sort(key=lambda student: student.split()[-1])
    return students


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)