#!/usr/bin/python3
"""writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a JSON representation of a given object"""

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
