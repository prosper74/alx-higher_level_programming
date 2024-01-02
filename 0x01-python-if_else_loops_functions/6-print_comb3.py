#!/usr/bin/python3
"""
Program that prints all possible different combinations of two digits.
Numbers must be separated by ,, followed by a space
The two digits must be different
01 and 10 are considered the same combination of the two digits 0 and 1
"""

for num1 in range(10):
    for num2 in range(num1 + 1, 10):
        if num1 == 8 and num2 == 9:
            print("{}{}".format(num1, num2))
        else:
            print("{}{}".format(num1, num2), end=", ")
