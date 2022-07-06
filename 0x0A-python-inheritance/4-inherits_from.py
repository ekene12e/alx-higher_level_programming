#!/usr/bin/python3
"""A class with a print sorted function
"""


def inherits_from(obj, a_class):
    """ checks for a kind of class"""

    obj_class = type(obj).__name__
    return issubclass(obj_class, a_class)
