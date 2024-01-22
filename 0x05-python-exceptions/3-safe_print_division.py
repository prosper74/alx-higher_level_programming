#!/usr/bin/python3


def safe_print_division(a, b):
    """Function that divides 2 integers and prints the result."""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
