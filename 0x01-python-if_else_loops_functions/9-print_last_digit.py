#!/usr/bin/python3
"""
Function that prints the last digit of a number
Returns the value of the last digit
"""


def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return (last_digit)
