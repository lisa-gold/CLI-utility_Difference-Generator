from gendiff.parser import get_content
from gendiff.formatters import format


def form_diff_dict(dict1, dict2):
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    keys_joined = list(set(keys1 + keys2))
    keys_joined.sort()
    diff_dict = {}
    for k in keys_joined:
        if k in set(keys1).difference(keys2):
            dict_for_key = fill_dict_for_key(k, 'deleted', dict1[k])
            diff_dict.update({k: dict_for_key})
        elif k in set(keys2).difference(keys1):
            dict_for_key = fill_dict_for_key(k, 'added', None, dict2[k])
            diff_dict.update({k: dict_for_key})
        elif dict1[k] == dict2[k]:
            dict_for_key = fill_dict_for_key(k, 'same', dict1[k], dict2[k])
            diff_dict.update({k: dict_for_key})
        elif isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
            child = form_diff_dict(dict1[k], dict2[k])
            dict_for_key = fill_dict_for_key(k, 'nested', children=child)
            diff_dict.update({k: dict_for_key})
        elif dict1[k] != dict2[k]:
            dict_for_key = fill_dict_for_key(k, 'updated', dict1[k], dict2[k])
            diff_dict.update({k: dict_for_key})
    return diff_dict


def fill_dict_for_key(key, type, old_value=None, new_value=None, children={}):
    return {'key': key,
            'type': type,
            'new_value': new_value,
            'old_value': old_value,
            'children': children
            }


def generate_diff(file_path1, file_path2, formatting='stylish'):
    """
    This function generates differance between two files in a choosen format
    """
    dict1 = get_content(file_path1)
    dict2 = get_content(file_path2)
    diff_dict = form_diff_dict(dict1, dict2)
    result = format.apply_format(diff_dict, formatting)
    return result
