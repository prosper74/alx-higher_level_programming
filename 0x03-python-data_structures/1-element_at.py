#!/usr/bin/python3
def element_at(my_list, idx):
    count = 0
    for i in my_list:
        if count == idx:
            return (i)
        count += 1
    return (None)
