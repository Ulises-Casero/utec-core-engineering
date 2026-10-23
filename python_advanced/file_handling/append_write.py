#!/usr/bin/env python3
"""""Módulo con función agrega una cadena al final de un archivo de texto."""


def append_write(filename="", text=""):
    """Agrega una cadena de texto al final del archivo."""
    nuevos_caracteres = len(text)
    with open(filename, "a") as file:
        file.write(text)
    return nuevos_caracteres
