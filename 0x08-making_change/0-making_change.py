#!/usr/bin/python3
""" Change comes from within
"""


def makeChange(coins, total):
    """ minimum change problem
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    score, i = 0, 0
    while total > 0:
        if i >= len(coins):
            return -1
        if (total - coins[i]) >= 0:
            score += 1
            total -= coins[i]
            i = 0
        else:
            i += 1
    return score
