
def collegeCourses(x, courses):
    """
    returns list of courses with names with a length not equal to x
    ----------
    parameters
    ----------
    courses:        list of course names
    x:              integer
    ----------
    >>> collegeCourses(7, ["Art", "Finance", "Business", "Speech",\
                           "History", "Writing", "Statistics"])
    ['Art', 'Business', 'Speech', 'Statistics']
    """
    def shouldConsider(course):
        return len(course) != x

    return list(filter(shouldConsider, courses))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)