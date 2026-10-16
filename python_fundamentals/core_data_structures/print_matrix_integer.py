#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    for elem in matrix:
        for i, elem2 in enumerate(elem):
            print("{:d}".format(elem2), end="")
            if i < len(elem) - 1:
                print(" ", end="")
        print()
