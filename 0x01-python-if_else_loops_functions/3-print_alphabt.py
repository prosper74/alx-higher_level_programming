#!/usr/bin/python3
""" Program that prints the ASCII alphabet, in lowercase. """

for alphabet in range(97, 123):
    if chr(alphabet) != 'q' and chr(alphabet) != 'e':
        print("{}".format(chr(alphabet)), end="")
