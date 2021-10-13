#!/usr/bin/python3
import json
"""
===================================================================
function that returns the JSON representation of an object (string)
===================================================================
"""


def to_json_string(my_obj):
    """ The JSON module is mainly used to convert the python
        dictionary above into a JSON string that can
        be written into a file.
    """

    return json.dumps(my_obj)
