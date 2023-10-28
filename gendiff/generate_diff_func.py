from gendiff.parser import get_content
from gendiff.formatters import format


def form_diff_dict(dict1, dict2):
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    keys_added = set(keys2).difference(keys1)
    keys_deleted = set(keys1).difference(keys2)
    keys_joined = keys1 + keys2
    keys_joined.sort()
    diff_dict = {}
    for k in keys_joined:
        if k in keys_deleted:
            dict_for_key = fill_dict_for_key(k, 'deleted', dict1, {k: None})
            diff_dict.update({k: dict_for_key})
        elif k in keys_added:
            dict_for_key = fill_dict_for_key(k, 'added', {k: None}, dict2)
            diff_dict.update({k: dict_for_key})
        elif dict1[k] == dict2[k]:
            dict_for_key = fill_dict_for_key(k, 'same', dict1, dict2)
            diff_dict.update({k: dict_for_key})
        elif isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
            dict_for_key = fill_dict_for_key(k, 'nested', dict1, dict2)
            diff_dict.update({k: dict_for_key})
        elif dict1[k] != dict2[k]:
            dict_for_key = fill_dict_for_key(k, 'updated', dict1, dict2)
            diff_dict.update({k: dict_for_key})
    return diff_dict


def fill_dict_for_key(key, type, old, new):
    if type != 'nested':
        children = []
        if isinstance(old[key], dict):
            children += list(old[key].keys())
        if isinstance(new[key], dict):
            children += list(new[key].keys())
        children = list(set(children))
        children.sort()
    else:
        children = form_diff_dict(old[key], new[key])
    diff_dict_key = {'key': key,
                     'type': type,
                     'new_value': new[key],
                     'old_value': old[key],
                     'children': children
                     }
    return diff_dict_key


def generate_diff(file_path1, file_path2, formatting='stylish'):
    """
    This function generates differance between two files in a choosen format
    """
    dict1 = get_content(file_path1)
    dict2 = get_content(file_path2)
    diff_dict = form_diff_dict(dict1, dict2)
    result = format.apply_format(diff_dict, formatting)
    return result
