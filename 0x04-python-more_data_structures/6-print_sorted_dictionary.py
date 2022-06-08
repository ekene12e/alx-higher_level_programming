#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a sorted dictionary by their keys"""
    if a_dictionary != {}:
        for key, value in sorted(a_dictionary.items()):
            print(f'{key}: {value}')
