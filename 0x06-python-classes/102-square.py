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
        self.size = size

    def __eq__(self, o):
        """Compares two square objects based on their area
        Returns: True Or False
        """
        return (self.area() == o.area())

    def __lt__(self, o):
        """Compares two squares based on their area
        """
        return (self.area() < o.area())

    def __le__(self, o):
        """Compares two squares based on their area
        """
        return (self.area() <= o.area())

    def __ge__(self, o):
        """Compares two squares based on their area
        """
        return (self.area() >= o.area())

    def __gt__(self, o):
        """Compares two squares based on their area
        """
        return (self.area() > o.area())

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
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns the area of the square
        """
        return self.__size * self.__size
