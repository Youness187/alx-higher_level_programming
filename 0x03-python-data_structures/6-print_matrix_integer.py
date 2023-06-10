#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for c in r:
            if c != r[-1]:
                print("{} ".format(c), end="")
            else:
                print("{}".format(c), end="")
        print()
