#!/usr/bin/python3
"""
Square module
"""
class Square:
    """Represent a square with a private size attribute."""
    def __init__(self, size):
        """Initialize a new Square instance with a private size attribute.
        The size is stored privately as an implementation detail and is not
        validated at this stage.
        """
        self.__size = size
