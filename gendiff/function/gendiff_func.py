from gendiff.function.open_files import open_file_as_dict
from gendiff.function.formatting import choose_format


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
        get_inner_change(diff_dict).update({key1: diff(dict1[key1],
                                            dict2[key1])})
    else:
        get_sub(diff_dict).update({key1: dict1[key1]})


def diff(dict1, dict2):
    diff_dict = form_diff_dict()
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    for k in keys1:
        fill_diff_dict(k, dict1, dict2, diff_dict)
    for k in keys2:
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
    dict1 = open_file_as_dict(file_path1)
    dict2 = open_file_as_dict(file_path2)
    diff_dict = diff(dict1, dict2)
    result = choose_format.apply_format(diff_dict, formatting)
    return result
