#!/usr/bin/python3

if __name__ == "__main__":
    """Performs basic operations on arguments passed """
    import sys
    import calculator_1 as op

    num_args = len(sys.argv) - 1
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if operator == '+':
        print("{} {} {} = {}".format(a, operator, b, op.add(a, b)))
    elif operator == '-':
        print("{} {} {} = {}".format(a, operator, b, op.sub(a, b)))
    elif operator == '*':
        print("{} {} {} = {}".format(a, operator, b, op.mul(a, b)))
    elif operator == '/':
        print("{} {} {} = {}".format(a, operator, b, op.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
