from gendiff.formatting import stylish
from gendiff import generate_diff_func


# Formater - plain
def modify_according_to_type(value):
    if value != stylish.transform_special_values(value):
        value_mod = stylish.transform_special_values(value)
    elif not isinstance(value, str):
        value_mod = value
    else:
        value_mod = f"'{value}'"
    return value_mod


def exchange_if_dict(object, value='[complex value]'):
    if isinstance(object, dict):
        return value
    else:
        return object


def overwrite_keys(key_outer, inner_dict):
    for key in inner_dict.keys():
        inner_keys = list(inner_dict[key].keys())
        for inner_key in inner_keys:
            new_key = '.'.join([key_outer, inner_key])
            inner_dict.get(key)[new_key] = inner_dict.get(key).pop(inner_key)


def style_plain_main(diff_dict):
    diff_dict_sorted = stylish.sort_alph(diff_dict)
    string = ''
    for k, val in diff_dict_sorted.items():
        v = modify_according_to_type(val)
        if k in generate_diff_func.get_add(diff_dict).keys():
            v = exchange_if_dict(v)
            string += f"Property '{k}' was added with value: {v}\n"
        if k in generate_diff_func.get_sub(diff_dict).keys():
            string += f"Property '{k}' was removed\n"
        if k in generate_diff_func.get_inner_change(diff_dict).keys():
            if not isinstance(v, dict):
                v_inner0 = modify_according_to_type(v[0])
                v_inner1 = modify_according_to_type(v[1])
                v_inner0 = exchange_if_dict(v_inner0)
                v_inner1 = exchange_if_dict(v_inner1)
                string += (f"Property '{k}' was updated. \
From {v_inner0} to {v_inner1}\n")
            else:
                overwrite_keys(k, v)
                string += style_plain_main(v)
    return string


def style_plain(diff_dict):
    string = style_plain_main(diff_dict)
    return string[:-1]
