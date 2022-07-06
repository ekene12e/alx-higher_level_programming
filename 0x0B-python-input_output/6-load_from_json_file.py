#!/usr/bin/python3
"""writes an Object to a text file,
using a JSON representation
"""
import json


def load_from_json_file(filename):
    """decodes a json file into objects"""

    with open(filename, 'r') as f:
        return json.load(f)
