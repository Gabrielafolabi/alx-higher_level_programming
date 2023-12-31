#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import sub, div, add, mul


if __name__ == "__main__":
    arglen = len(argv) - 1
    if arglen == 0:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    operator = argv[2]
    a, b = int(argv[1]), int(argv[3])
    if operator == "+":
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif operator == "-":
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif operator == "*":
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    elif operator == "/":
        print('{} / {} = {}'.format(a, b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
