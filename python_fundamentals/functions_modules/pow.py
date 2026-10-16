#!/usr/bin/env python3

def pow(a, b):
    result = 1

    if b != 0:
        result = a

    for _ in range(b-1):
        result *= a
    return result
