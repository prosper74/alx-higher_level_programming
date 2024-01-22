#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Function that divides element by element 2 lists."""

    result_list = []

    try:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            except (ValueError, TypeError):
                print("wrong type")
                result = 0
            except IndexError:
                print("out of range")
                result = 0
            finally:
                result_list.append(result)
    finally:
        return result_list
