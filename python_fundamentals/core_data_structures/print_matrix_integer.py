#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    for elem in matrix:
        for i, elem2 in enumerate(elem):
            print("{}".format(elem2), end="")
            if i < len(row) - 1:
                print(" ", end="")
        print()
