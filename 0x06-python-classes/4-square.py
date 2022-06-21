#!/usr/bin/python3
"""An square module that initializes
    a square
"""


class Square:
    '''
    Defines a square
    '''
    def __init__(self, size=0):
        """
        INSTATIATES a new square

        Args:
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """private instance attribute

        Returns:
            int: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of square

        Args:
            value (int): value to set

        Raises:
            TypeError: error
            ValueError: error
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns the area of the square
        """
        return self.__size * self.__size
