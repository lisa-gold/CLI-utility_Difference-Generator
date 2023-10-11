from gendiff.function.formatting import stylish
from gendiff.function.formatting import plain
from gendiff.function.formatting import json


def apply_format(diff, format):
    if format == 'stylish':
        return stylish.style(diff)
    elif format == 'plain':
        return plain.style_plain(diff)
    elif format == 'json':
        return json.style_json(diff)
    else:
        return 'Wrong format name!\n Supported formats: stylish, plain, json.'
