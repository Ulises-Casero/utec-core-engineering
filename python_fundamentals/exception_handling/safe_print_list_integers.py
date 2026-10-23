#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    contador = 0
    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                contador += 1
        except IndexError:
            break 
        print()
    return contador
