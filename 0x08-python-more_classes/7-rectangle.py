#!/usr/bin/python3
"""describes a class
of rectangle


"""


class Rectangle:
    """rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if 0 in (self.__width, self.__height):
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        if 0 in (self.__width, self.__height):
            return ""
        for i in range(self.__height):
            rect = []
            for i in range(self.__height):
                [rect.append(Rectangle.print_symbol) for j in range(self.__width)]

                if i != self.__height - 1:
                    rect.append("\n")

        return ("".join(rect))

    def __repr__(self):
        """representation of the class"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        '''method: __del__
        deletes instance of Rectangle class, and prints "bye" message
        '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
