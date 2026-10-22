#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        contador = 0
        for i in range(x):
            if type(my_list) == int:
                print(my_list[i], end="")
                contador += 1
        return contador
    except IndexError:
        return None