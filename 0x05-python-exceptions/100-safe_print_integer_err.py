#!/usr/bin/python3


def safe_print_integer_err(value):
    if value:
        try:
            print("{:d}".format(value))
            return True
        except TypeError as err:
            print("Exception: {}".format(err))
            return False
