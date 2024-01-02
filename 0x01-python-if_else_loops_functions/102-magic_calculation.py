#!/usr/bin/python3
"""
function that does exactly the same as the Python bytecode.
"""


def magic_calculation(a, b, c):
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    a = a * b
    a = a - c
    return (a)
