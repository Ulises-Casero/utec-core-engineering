#!/usr/bin/env python3
"""""Módulo con función añade una cadena al final de un archivo de texto."""


def write_file(filename="", text=""):
    """Añade una cadena de texto al final del archivo."""
    nuevos_caracteres = len(text)
    with open(filename, "a") as file:
        file.write(text)
    return nuevos_caracteres
