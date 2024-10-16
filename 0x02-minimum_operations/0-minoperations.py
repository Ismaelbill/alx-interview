#!/usr/bin/python3
""" Minimum Operations """


def prime_factors(n):
    """ pre-defined function for prime factors,
    returns list if n is prime"""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return factors


def minOperations(n):
    """minOperations - func that calculates
    the fewest number of operations needed
    to result in exactly n H characters in the file."""
    if n > 1:
        result = prime_factors(n)
        if len(result) > 1:
            num = 0
            for i in result:
                num += i
            return num
    return 0
