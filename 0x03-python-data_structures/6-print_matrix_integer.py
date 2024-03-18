#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        j = 0
        for i in n:
            if j < len(n) - 1:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
            j += 1
        print()
