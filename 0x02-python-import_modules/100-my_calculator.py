#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    length = len(sys.argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    def printSum(na, nb, op, fun):
        print("{0} {1} {2} = {3}".format(na, op, nb, fun(na, nb)))

    if operator == "+":
        printSum(a, b, operator, add)
    elif operator == "-":
        printSum(a, b, operator, sub)
    elif operator == "*":
        printSum(a, b, operator, mul)
    elif operator == "/":
        printSum(a, b, operator, div)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
