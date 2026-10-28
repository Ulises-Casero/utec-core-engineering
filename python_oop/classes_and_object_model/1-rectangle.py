#!/usr/bin/env python3
"""Define la clase Rectangle """


class Rectangle():
    """Declaración de la clase Rectangle ."""

    def __innit__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value=0):
        if type(value) is not int:
            raise TypeError()("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value=0):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = value
