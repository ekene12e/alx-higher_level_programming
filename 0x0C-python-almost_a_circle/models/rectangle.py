#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instatiates a new Rectangle"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of the rectangle"""

        return self.width * self.height

    def display(self):
        """display the rectangle"""
        for i in range(self.y):
            print('\n', end='')
        for i in range(self.height):
            print(f'{" " * self.x}{"#" * self.width}')

    def __str__(self):
        return f'[{self.__class__.__name__}] \
({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """Update the rectangle parameters"""
        
        if args is not None and len(list(args)) > 0:
            values = list(args)
            value_len = len(values)

            att_list = ['id', 'width', 'height', 'x', 'y']
            for i in range(value_len):
                setattr(self, att_list[i], values[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary representation of rect"""
        
        list_attr = ['id', 'width', 'height', 'x', 'y']
        dict_rect = {}

        for key in list_attr:
            dict_rect[key] = getattr(self, key)
        return dict_rect
