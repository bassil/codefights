from itertools import combinations

def crazyball(players, k):
    return [list(lineup) for lineup in combinations(sorted(players), k)]
