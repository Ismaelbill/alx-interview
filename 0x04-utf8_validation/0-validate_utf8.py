#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """method that determines if a given data set
    represents a valid UTF-8 encoding"""
    return check(data)


def check(data):
    """ checks data if valid"""
    i = 0
    for d in data:
        bnr = bin(d)[2:]
        length = len(bnr)
        if length <= 8:
            i = 0
            while i < length and '0' != bnr[i]:
                i += 1
            if not (i >= 0 and i <= 4):
                return False
    return True
