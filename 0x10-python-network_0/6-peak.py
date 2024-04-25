#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    new_list = list_of_integers
    beg = 0
    end = len(new_list)-1

    if new_list[beg] > new_list[beg+1]:
        return new_list[beg]
    if new_list[end] > new_list[end-1]:
        return new_list[end]

    mid = (beg+end)//2
    if new_list[mid-1] < new_list[mid] and new_list[mid+1] < new_list[mid]:
        return new_list[mid]
    if new_list[mid] < new_list[mid-1]:
        return find_peak(new_list[beg:mid+1])
    elif new_list[mid] < new_list[mid+1]:
        return find_peak(new_list[mid:end+1])
    else:
        return new_list[beg]
