from gendiff.open_files import open_file
from gendiff.formatting import format


def form_diff_dict():
    diff_dict = {'no_change': {},
                 'add': {},
                 'sub': {},
                 'inner_change': {}
                 }
    return diff_dict


def fill_diff_dict(key1, dict1, dict2, diff_dict):
    keys2 = list(dict2.keys())
    if key1 in keys2 and dict1[key1] == dict2[key1]:
        get_no_change(diff_dict).update({key1: dict1[key1]})
    elif (key1 in keys2 and dict1[key1] != dict2[key1]
          and (not isinstance(dict1[key1], dict)
          or not isinstance(dict2[key1], dict))):
        get_inner_change(diff_dict).update({key1: (dict1[key1], dict2[key1])})
    elif (key1 in keys2 and dict1[key1] != dict2[key1]
          and isinstance(dict1[key1], dict) and isinstance(dict2[key1], dict)):
        get_inner_change(diff_dict).update({key1: fill_diff(dict1[key1],
                                            dict2[key1])})
    else:
        get_sub(diff_dict).update({key1: dict1[key1]})


def fill_diff(dict1, dict2):
    diff_dict = form_diff_dict()
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    keys_joined = keys1 + keys2
    for k in keys_joined:
        if k in keys1:
            fill_diff_dict(k, dict1, dict2, diff_dict)
        if k not in keys1:
            get_add(diff_dict).update({k: dict2[k]})
    return diff_dict


# Getters
def get_no_change(dictionary):
    return dictionary['no_change']


def get_add(dictionary):
    return dictionary['add']


def get_sub(dictionary):
    return dictionary['sub']


def get_inner_change(dictionary):
    return dictionary['inner_change']


# Opening and formatting
def generate_diff(file_path1, file_path2, formatting='stylish'):
    """
    This function generates differance between two files in a choosen format
    """
    dict1 = open_file(file_path1)
    dict2 = open_file(file_path2)
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        if not isinstance(dict1, dict):
            return dict1
        return dict2
    diff_dict = fill_diff(dict1, dict2)
    result = format.apply_format(diff_dict, formatting)
    return result
