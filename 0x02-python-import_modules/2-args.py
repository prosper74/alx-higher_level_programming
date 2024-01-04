#!/usr/bin/python3
"""
Program that prints the number of and the list of its arguments
"""
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv) - 1
    print("{:d} ".format(arg_count), end="")
    if arg_count == 0:
        print("argument.")
    else:
        if arg_count == 1:
            print("argument:".format(arg_count))
        else:
            print("arguments:".format(arg_count))
        for i in range(1, len(sys.argv)):
            print("{:d}: {}".format(i, sys.argv[i]))
