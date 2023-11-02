import os
import json
import yaml


def parse_as_dict(content, extension):
    if extension == 'json':
        return json.load(content)
    elif extension in ['yml', 'yaml']:
        return yaml.safe_load(content)
    raise Exception(
        'Wrong extension! Supported extensions: json, yml, yaml')


def get_content(file_path):
    _, extension = os.path.splitext(file_path)
    with open(file_path) as file:
        return parse_as_dict(file, extension[1:])
