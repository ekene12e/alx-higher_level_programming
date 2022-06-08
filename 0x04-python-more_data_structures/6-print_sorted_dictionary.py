#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary != {}:
        for key, value in a_dictionary.items().sorted():
            print(f'{key}: {value}')
