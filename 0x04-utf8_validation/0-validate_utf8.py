#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """method that determines if a given data set
    represents a valid UTF-8 encoding"""
    for d in data:
        if not (0 <= d <= 255):
            return False
    return True
