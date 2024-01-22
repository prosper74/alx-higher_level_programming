#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        max_key = max(a_dictionary, key=a_dictionary.get)
        return max_key

    return None
