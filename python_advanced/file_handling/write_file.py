#!/usr/bin/env python3
"""""Módulo con función escribir una cadena en un archivo de texto."""


def write_file(filename="", text=""):
    """Inserta una cadena en un archivo."""
    caracteres = len(text)
    with open(filename, "w") as file:
        file.write(text)
    return caracteres
