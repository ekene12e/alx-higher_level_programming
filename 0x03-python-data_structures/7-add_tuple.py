#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a(0):
        a1 = 0
    else:
        a1 = tuple_a(0)

    if not tuple_a(1):
        a2 = 0
    else:
        a2 = tuple_a(1)

    if not tuple_b(0):
        b1 = 0
    else:
        b1 = tuple_b(0)

    if not tuple_b(1):
        b2 = 0
    else:
        b2 = tuple_b(1)

    new_t = (a1 + b1, a2 + b2)
    return new_t