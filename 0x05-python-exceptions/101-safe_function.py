#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Function that executes a function safely."""
    try:
        return fct(*args)
    except Exception as e:
        error = "Exception: " + str(e) + "\n"
        sys.stderr.write(error)
        return None
