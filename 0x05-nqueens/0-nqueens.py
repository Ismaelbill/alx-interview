#!/usr/bin/python3
"""
The N queens puzzle is the challenge
of placing N non-attacking queens on an N×N chessboard.
"""
import sys


args = sys.argv[1:]
length = len(args)
if length == 0 or length > 1:
    print("Usage: nqueens N")
    exit(1)

n = args[0]

try:
    n = int(n)
except ValueError:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)

col = set()
posDiag = set()
negDiag = set()

res = []
board = [[] * n for _ in range(n)]


def nQueen(r):
    """nqueen - func that uses backtracking to find all
        posibilities
    """
    if r == n:
        cp = [row for row in board]
        res.append(cp)
        return

    for c in range(n):
        if c in col or (r + c) in posDiag or (r - c) in negDiag:
            continue

        col.add(c)
        posDiag.add(r + c)
        negDiag.add(r - c)
        board[r] = [r, c]

        nQueen(r + 1)

        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)
        board[r] = '.'


nQueen(0)
for r in res:
    print(r)
