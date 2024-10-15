#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """minOperations - func that calculates
    the fewest number of operations needed
    to result in exactly n H characters in the file."""
    if n <= 0:
        return 0

    if n == 2:
        return 2
    arr = []
    for i in range(2, n):
        val = (n // i) + i
        arr.append(val)
    return min(arr)
