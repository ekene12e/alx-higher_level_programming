#!/usr/bin/python3
"""An square module that initializes
    a square
"""


class Square:
    '''
    Defines a square
    '''
    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiates a new square

        Args:
            size (int): size of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''gets the position
        '''
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        if not (value[0] >= 0 and value[1] >= 0):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """Returns the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using #
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
