#!/usr/bin/python3
"""Prints a hello message with first and last name


  args: Firstname
        lastname
"""


def say_my_name(first_name, last_name=""):
    """prints a hello msg
    Args:
        first_name (str): first name
        last_name (str, optional): last name. Defaults to "".
    """

    if first_name == '' and last_name:
        first_name = last_name
        last_name = ''

    name = [first_name, last_name]
    for i in name:
        if not isinstance(i, str):
            if name.index(i) == 0:
                err = "first_name"
            else:
                err = "last_name"
            err
            raise TypeError(f'{err} must be a string')
    if last_name:
        print("My name is {} {}".format(name[0], name[1]))
    else:
        print("My name is {}".format(name[0]))
