#!/usr/bin/python3
"""
Program that prints numbers from 01 to 99
Numbers must be separated by ,, followed by a space.
"""

for i in range(100):
    if i == 99:
        print("{}".format(i))

    print("{:02}".format(i), end=", ")
