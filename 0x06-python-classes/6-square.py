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
        INSTATIATES a new square

        Args:
            size (int): size of square
        """
        self.__size = size
        self.__position = position

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
        '''gets the position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''sets the position atribute'''

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError('position must be a tuple of 2 positive \
integers')
        self.__position = value

    def area(self):
        """Returns the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using #
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
