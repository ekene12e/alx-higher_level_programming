#!/usr/bin/python3
"""A class with a print sorted function
"""


def inherits_from(obj, a_class):
    """ checks for a kind of class"""

    obj_class = type(obj)
    if obj_class == a_class:
        return False
    return issubclass(obj_class, a_class)
