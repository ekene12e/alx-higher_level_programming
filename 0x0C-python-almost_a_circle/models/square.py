#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
        self.width = value
        self.height = value

    def __str__(self):
        return f'[{self.__class__.__name__}] \
({self.id}) {self.x}/{self.y} - {self.width}'

    def update(self, *args, **kwargs):
        """Update the rectangle parameters"""

        if args is not None and len(list(args)) > 0:
            values = list(args)
            value_len = len(values)

            att_list = ['id', 'size', 'x', 'y']
            for i in range(value_len):
                setattr(self, att_list[i], values[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of square"""

        list_attr = ['size', 'id', 'x', 'y']
        dict_sq = {}

        for key in list_attr:
            dict_sq[key] = getattr(self, key)
        return dict_sq
