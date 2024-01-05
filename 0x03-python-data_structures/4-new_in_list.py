#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]

    for i in range(len(dir(my_list))):
        if i == idx:
            new_list[i] = element

    return (new_list)
