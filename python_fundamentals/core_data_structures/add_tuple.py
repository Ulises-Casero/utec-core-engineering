#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):

    valor_1 = tuple_a[0] if len(tuple_a) > 0 else 0
    valor_2 = tuple_a[1] if len(tuple_a) > 1 else 0

    valor_3 = tuple_b[0] if len(tuple_b) > 0 else 0
    valor_4 = tuple_b[1] if len(tuple_b) > 1 else 0

    resultado_1 = valor_1 + valor_3
    resultado_2 = valor_2 + valor_4

    return resultado_1, resultado_2
