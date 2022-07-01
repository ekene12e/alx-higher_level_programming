#!/usr/bin/python3
"""Prints a square of a given size


  args: size(int)

"""


def print_square(size):
    """prints a square

    Args:
        size (int): size of the square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        return
    for i in range(size):
        print("#" * size)
