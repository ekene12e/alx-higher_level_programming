#!/usr/bin/python3
"""A class with a print sorted function
"""


class MyList(list):
    """A list of objects"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
