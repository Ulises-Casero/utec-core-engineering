#!/usr/bin/env python3
"""Define la clase Square"""


class Square():
    """Declaración de la clase Square."""

    def __init__(self, size=0, position = (0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        return self.__position
        
    @position.setter
    def position(self, position = (0, 0)):
        if not isinstance(position, tuple) or len(position) != 2 or any(not isinstance(x, int) or x < 0 for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return (self.size * self.size)

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()

            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
    
    def __str__(self):
        if self.size == 0:
            return ""

        rows = []

        for _ in range(self.position[1]):
            rows.append("")

        for _ in range(self.size):
            rows.append(" " * self.position[0] + "#" * self.size)

        return "\n".join(rows)
