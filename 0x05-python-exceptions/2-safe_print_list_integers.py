#!/usr/bin/python3


def safe_print_list_integers(my_list=None, x=0):
    """Function that prints the first x elements
    of a list and only integers."""

    if my_list is None:
        my_list = []

    count_integers = 0

    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count_integers += 1
        print()
        return count_integers
    except (IndexError, ValueError, TypeError):
        print()
        return count_integers
