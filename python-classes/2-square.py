#!/usr/bin/python3
"""
Square module
"""


class Square:
    """Represent a square with a private size attribute."""
    def __init__(self, size=0):
        """Initialize a new Square instance with a private size attribute.
        The size is stored privately as an implementation detail and is not
        validated at this stage.
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
