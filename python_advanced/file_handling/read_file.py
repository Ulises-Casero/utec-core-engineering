#!/usr/bin/env python3
"""Módulo con función para leer un archivo de texto."""


def read_file(filename=""):
    with open(filename, "r") as file:
        contenido = file.read()
    print(contenido, end="")
