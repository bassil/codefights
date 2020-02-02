def createSpiralMatrix(n):
    """
    return an n by n matrix with values starting in the bottom right corner
    and increasing in a counter-clockwise spiral
    ----------
    parameters
    ----------
    n:      integer
    ----------
    >>> createSpiralMatrix(3)
    [[5, 4, 3], [6, 9, 2], [7, 8, 1]]
    """
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    curDir = 0
    curPos = (n - 1, n - 1)
    res = [[0]*n for i in range(n)]

    for i in range(1, n * n + 1):
        res[curPos[0]][curPos[1]] = i
        nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        if not (0 <= nextPos[0] < n and
                0 <= nextPos[1] < n and
                res[nextPos[0]][nextPos[1]] == 0):
            curDir = (curDir + 1) % 4
            nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        curPos = nextPos

    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)