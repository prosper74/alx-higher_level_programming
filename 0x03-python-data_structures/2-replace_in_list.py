#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    count = 0
    for ele in my_list:
        if count == idx:
            my_list[count] = element
            return (my_list)
        count += 1
    return (my_list)
