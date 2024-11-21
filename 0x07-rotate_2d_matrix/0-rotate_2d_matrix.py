#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """ function for rotating a 2d list """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    for i in range(n):
        matrix[i] = list(reversed(matrix[i]))
    return matrix
