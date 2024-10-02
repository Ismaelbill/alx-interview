#!/usr/bin/python3

""" pascal triangle """

from math import factorial


def pascal_triangle(n):
    """ function returns list of lists of integers representing
    the pascal's trangle of 'n' by using binomial coefficient formula """
    if n <= 0:
        return []
    arr = []
    nestArr = []
    for i in range(n):
        for j in range(i+1):
            ncr = factorial(i) // (factorial(j) * factorial(i - j))
            print(i, j)
            nestArr.append((ncr))
        arr.append(nestArr)
        nestArr = []
    return arr
