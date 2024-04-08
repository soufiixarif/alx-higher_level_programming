#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    c = len(sys.argv)
    if c != 4:
        print("sage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operation = sys.argv[2]
    if operation == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
        sys.exit(0)
    elif operation == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
        sys.exit(0)
    elif operation == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
        sys.exit(0)
    elif operation == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
        sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
