#!/usr/bin/python3
"""
function that converts a string to uppercase
"""


def uppercase(s):
    result = ""
    for char in s:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            uppercase_ascii = ascii_value - 32
            result += "{}".format(chr(uppercase_ascii))
        else:
            result += "{}".format(char)
    print(result)
