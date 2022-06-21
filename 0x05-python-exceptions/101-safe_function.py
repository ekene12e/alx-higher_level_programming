#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function safely

    Args:
        fct: function to be executed
        args: arguments to fct

    Return: return value of fct or None if any error
    """
    try:
        return fct(*args)
    except BaseException as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
