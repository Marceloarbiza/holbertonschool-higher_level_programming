#!/usr/bin/python3
"""
==========================================================================
function that writes an Object to a text file, using a JSON representation
==========================================================================
"""
import json


def save_to_json_file(my_obj, filename):
    """ The dump() function is used to serialize data.
        It takes a Python object, serializes it and writes
        the output (which is a JSON string) to a file like object.
    """

    with open(filename, 'w') as outfile:
        return json.dump(my_obj, outfile)
