from gendiff.formatting import stylish
from gendiff.formatting import plain
from gendiff.formatting import json


def apply_format(diff, format):
    if format == 'stylish':
        return stylish.style(diff)
    elif format == 'plain':
        return plain.style_plain(diff)
    elif format == 'json':
        return json.style_json(diff)
    else:
        raise Exception
