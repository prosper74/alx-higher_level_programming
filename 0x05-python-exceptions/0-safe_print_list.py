#!/usr/bin/python3


def safe_print_list(my_list=None, x=0):
    """Function that prints x elements of a list."""

    if my_list is None:
        my_list = []

    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count
