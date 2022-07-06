#!/usr/bin/python3


def read_file(filename=""):
    """reads and prints a file"""

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
