#!/usr/bin/env python3

def safe_print_division(a, b):
    resultado = 0
    try:
        resultado = a / b
    except (TypeError, ZeroDivisionError):
        resultado = None
    finally:
        print("Inside result: {}".format(resultado))
        print("{:d} / {:d} = {}".format(a,b,resultado))
