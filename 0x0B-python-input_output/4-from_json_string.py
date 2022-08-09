#!/usr/bin/python3
"""returns json of an object"""
import json


def from_json_string(my_str):
    """returns object from json string"""

    return json.loads(my_str)
