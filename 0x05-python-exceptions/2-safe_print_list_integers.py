#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    try:
        printed_int = 0
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end='')
                printed_int += 1
            except (ValueError):
                continue
        return printed_int
    except IndexError:
        return printed_int
