from gendiff.formatters import stylish
from gendiff.formatters import plain
from gendiff.formatters import json


def apply_format(diff, format):
    if format == 'stylish':
        return stylish.build_stylish(diff)
    elif format == 'plain':
        return plain.build_plain_style(diff)
    elif format == 'json':
        return json.build_json(diff)
    else:
        raise Exception('Wrong format! Supported formats: stylish, plain, json')
