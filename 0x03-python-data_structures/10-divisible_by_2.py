#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []

    for num in my_list:
        result.append(num % 2 == 0)

    return result
