#!/usr/bin/python3
""" 0. Prime Game
"""


def isWinner(x, nums):
    """ function that returns the winner in the game
    """
    i = 0
    players = {'Maria': 0, 'Ben': 0}
    while x:
        prime_nums = []
        remaining_nums = []
        for j in range(1, nums[i] + 1):
            if is_prime(j):
                prime_nums.append(j)
            remaining_nums.append(j)

        ret = track(prime_nums, remaining_nums)
        if ret % 2 == 0:
            players['Maria'] += 1
        else:
            players['Ben'] += 1
        i += 1
        x -= 1
    if players['Maria'] > players['Ben']:
        return 'Ben'
    else:
        return 'Maria'


def track(pr, arr):
    copy_arr = arr[:]
    k = 0
    for p_num in pr:
        for i in range(len(arr)):
            if arr[i] % p_num == 0:
                # print(i)
                if arr[i] in copy_arr:
                    copy_arr.remove(arr[i])
        k += 1
    return k


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
