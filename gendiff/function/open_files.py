import os
import json
import yaml


def define_extension(file_path):
    return os.path.splitext(file_path)[-1]


def open_file_as_dict(file_path):
    result = {}
    extension = define_extension(file_path)
    if extension == '.json':
        result = json.load(open(file_path))
    elif extension in ['.yml', '.yaml']:
        with open(file_path) as f:
            result = yaml.safe_load(f)
    else:
        result = 'Wrong extention! Supported extensions: json, yaml, yml.'
    return result
