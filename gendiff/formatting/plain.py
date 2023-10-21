from gendiff.formatting import stylish


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
    inner_keys = list(inner_dict.keys())
    for inner_key in inner_keys:
        new_key = '.'.join([key_outer, inner_key])
        inner_dict[new_key] = inner_dict.pop(inner_key)


def style_plain_main(diff_dict):
    string = ''
    for k, val in diff_dict.items():
        v_new = modify_according_to_type(val['new_value'])
        v_old = modify_according_to_type(val['old_value'])
        v_new = exchange_if_dict(v_new)
        v_old = exchange_if_dict(v_old)
        if val['type'] == 'added':
            string += f"Property '{k}' was added with value: {v_new}\n"
        if val['type'] == 'deleted':
            string += f"Property '{k}' was removed\n"
        if val['type'] == 'updated':
            if v_old == '[complex value]' and v_new == '[complex value]':
                overwrite_keys(k, val['children'][0])
                string += style_plain_main(val['children'][0])
            else:
                string += (f"Property '{k}' was updated. \
From {v_old} to {v_new}\n")
    return string


def style_plain(diff_dict):
    string = style_plain_main(diff_dict)
    return string[:-1]
