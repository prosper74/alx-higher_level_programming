#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or not my_list:
        return my_list

    new_list = del my_list[idx]

    return new_list
