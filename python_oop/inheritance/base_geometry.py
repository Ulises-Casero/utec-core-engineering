#!/usr/bin/env python3
"""Esta clase implementara metos para heredar"""


class BaseGeometry():
    """La clase implementara metodos que las clases hijas heredaran."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
