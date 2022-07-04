#!/usr/bin/python3
"""Looks up the attributes of a given class
"""


class MyList(list):
    """A list of objects"""

    def print_sorted(self):
        """Prints a sorted list"""
        a = self
        print(a.sort())
