#!/usr/bin/python3


def safe_print_integer(value):
    """Function to print true or false if integer value"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
