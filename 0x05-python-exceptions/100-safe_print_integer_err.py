#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Function that prints an integer"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        error = "Exception: " + str(e) + "\n"
        sys.stderr.write(error)
        return False
