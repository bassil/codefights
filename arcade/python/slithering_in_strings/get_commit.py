def getCommit(commit):
    return commit.translate({ord(c): None for c in "0?+!"})

print(getCommit("0??+0+!!someCommIdhsSt"))
