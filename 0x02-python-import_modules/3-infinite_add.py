#!/usr/bin/python3
"""
Program that prints the result of the addition of all arguments
The output is the result of the addition of all arguments
"""
if __name__ == "__main__":
    import sys
    sum = 0
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])
    print("{:d}".format(sum))
