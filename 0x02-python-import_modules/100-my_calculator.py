#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit


def main():
    if len(argv) - 1 != 3:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        val = add(a, b)
    elif argv[2] == '-':
        val = sub(a, b)
    elif argv[2] == '*':
        val = mul(a, b)
    elif argv[2] == '/':
        val = div(a, b)
    else:
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)
    print("{:d} {} {:d} = {:d}".format(a, argv[2], b, val))


if __name__ == "__main__":
    main()
