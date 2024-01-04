#!/usr/bin/python3
import sys


def main():
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


if __name__ == "__main__":
    main()
