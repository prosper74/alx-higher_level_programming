#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    if key and key in a_dictionary:
        del a_dictionary[key]
