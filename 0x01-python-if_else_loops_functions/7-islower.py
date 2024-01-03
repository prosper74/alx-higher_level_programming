#!/usr/bin/python3
"""
function that checks for lowercase characters
You are not allowed to use this function islower fuction
"""


def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False
