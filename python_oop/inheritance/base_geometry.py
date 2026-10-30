#!/usr/bin/env python3
"""El propósito de esta clase es proporcionar funcionalidad compartida que las subclases puedan reutilizar"""


class BaseGeometry():
    """La clase implementara metodos que las clases hijas heredaran."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
