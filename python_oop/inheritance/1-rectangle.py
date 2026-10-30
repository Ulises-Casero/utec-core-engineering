#!/usr/bin/env python3
"""Este archivo contendra todo lo vinculado a la clase rectangle."""


BaseGeometry = __import__('base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Representa un rectangulo."""


    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
