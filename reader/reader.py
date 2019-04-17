import os
import json


def read(file_name):
    """"
    Load a mock file from os and return parsed json.
    """
    json_file = open(os.path.dirname(os.path.abspath(file_name)) + '\mocks\\' + file_name + '.json')
    data = json.load(json_file)
    json_file.close()

    return data




