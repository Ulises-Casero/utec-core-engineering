#!/usr/bin/env python3
"""Este archivo contendra todo lo vinculado a la clase Square."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado."""

    def __init__(self, size):
        self.integer_validator("Square", size)
        self.__size = size

    def area(self):
        resultado = self.__size * self.__size
        return resultado
