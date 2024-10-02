#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    function returns list of lists of integers
    representing the pascal's trangle of 'n'
    by using binomial coefficient formula
    """
    if n <= 0:
        return []
    arr = [[1]]
    for i in range(n - 1):
        tmp = [0] + arr[-1] + [0]
        row = []
        for j in range(len(arr[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        arr.append(row)
    return arr
