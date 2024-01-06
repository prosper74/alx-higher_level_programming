#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    count = 0

    for _ in my_list:
        if count == idx:
            new_list[count] = element
        count += 1
    return (new_list)
