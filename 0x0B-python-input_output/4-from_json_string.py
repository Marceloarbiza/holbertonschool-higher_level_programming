#!/usr/bin/python3
import json
"""
================
function that returns an object (Python data structure)
represented by a JSON string
================
"""


def from_json_string(my_str):
    """ The JSON module can also take a JSON
    string and convert it back to a dictionary structure
    """

    return json.loads(my_str)
