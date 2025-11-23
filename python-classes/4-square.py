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
        self.__size = size

    def area(self):
        """
        Method that returns area of square defined by size
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Setter and Getter for size value since it private
        """
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print(self.__size * '#')
