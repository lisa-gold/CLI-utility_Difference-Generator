import os
import json
import yaml


def define_extension(file_path):
    return os.path.splitext(file_path)[-1]


def parse_as_dict(content, extension):
    if extension == '.json':
        return json.load(content)
    elif extension in ['.yml', '.yaml']:
        return yaml.safe_load(content)
    else:
        return 'Wrong extention! Supported extensions: json, yaml, yml.'


def open_file(file_path):
    extension = define_extension(file_path)
    with open(file_path) as file:
        return parse_as_dict(file, extension)
