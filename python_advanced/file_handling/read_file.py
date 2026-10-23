#!/usr/bin/env python3

def read_file(filename=""):
    with open(filename, "r") as file:
        contenido = file.read()
    print(contenido, end="")
