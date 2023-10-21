from gendiff.file_opener import open_file
from gendiff.formatting import format


def form_dict_for_key(name, type, new_value, old_value, children):
    diff_dict = {'key': name,
                 'type': type,
                 'new_value': new_value,
                 'old_value': old_value,
                 'children': children
                 }
    return diff_dict


def fill_dict_for_key(key, type, old, new):
    children = []
    if isinstance(old[key], dict):
        children_old = list(old[key].keys())
        children += children_old
    if isinstance(new[key], dict):
        childern_new = list(new[key].keys())
        children += childern_new
    children = list(set(children))
    children.sort()
    diff_dict_key = form_dict_for_key(key, type, new[key], old[key], children)
    return diff_dict_key


def sort_alph(diff_dict):
    keys_in_result = list(diff_dict.keys())
    keys_in_result.sort()
    sorted_dict = {k: diff_dict[k] for k in keys_in_result}
    return sorted_dict


def form_diff_dict(dict1, dict2):
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    keys_joined = keys1 + keys2
    diff_dict = {}
    for k in keys_joined:
        fill_diff_dict(k, dict1, dict2, diff_dict)
    diff_dict = sort_alph(diff_dict)
    return diff_dict


def fill_diff_dict(k, dict1, dict2, diff_dict):
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    if k in keys1 and k in keys2 and dict1[k] == dict2[k]:
        dict_for_key = fill_dict_for_key(k, 'same', dict1, dict2)
        diff_dict.update({k: dict_for_key})
    if k in keys1 and k in keys2 and dict1[k] != dict2[k]:
        if not isinstance(dict1[k], dict) or not isinstance(dict2[k], dict):
            dict_for_key = fill_dict_for_key(k, 'updated', dict1, dict2)
            diff_dict.update({k: dict_for_key})
        else:
            dict_for_key = fill_dict_for_key(k, 'updated', dict1, dict2)
            diff_dict.update({k: dict_for_key})
            dict_for_key_inner = form_diff_dict(dict1[k], dict2[k])
            diff_dict[k]['children'] = [dict_for_key_inner]
            diff_dict[k]['children'].sort()
    if k in keys1 and k not in keys2:
        dict_for_key = fill_dict_for_key(k, 'deleted', dict1, {k: None})
        diff_dict.update({k: dict_for_key})
    if k not in keys1:
        dict_for_key = fill_dict_for_key(k, 'added', {k: None}, dict2)
        diff_dict.update({k: dict_for_key})


def generate_diff(file_path1, file_path2, formatting='stylish'):
    """
    This function generates differance between two files in a choosen format
    """
    dict1 = open_file(file_path1)
    dict2 = open_file(file_path2)
    diff_dict = form_diff_dict(dict1, dict2)
    result = format.apply_format(diff_dict, formatting)
    return result
