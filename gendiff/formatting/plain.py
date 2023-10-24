from gendiff.formatting import stylish


# Formater - plain
def modify_according_to_type(value):
    if isinstance(value, dict):
        value_mod = '[complex value]'
    elif value != stylish.transform_special_values(value):
        value_mod = stylish.transform_special_values(value)
    elif not isinstance(value, str):
        value_mod = value
    else:
        value_mod = f"'{value}'"
    return value_mod


def style_plain(diff_dict):
    differences = []
    for k, val in diff_dict.items():
        style_plain_list(k, val, differences)
        differences = list(filter(lambda x: x is not None, differences))
    return "\n".join(differences)


def style_plain_list(k, val, differences):
    v_new = modify_according_to_type(val['new_value'])
    v_old = modify_according_to_type(val['old_value'])
    if val['type'] == 'added':
        differences.append(f"Property '{k}' was added with value: {v_new}")
    if val['type'] == 'deleted':
        differences.append(f"Property '{k}' was removed")
    if val['type'] == 'updated':
        differences.append((f"Property '{k}' was updated. \
From {v_old} to {v_new}"))
    if val['type'] == 'nested':
        for inner_key, inner_val in val["children"][0].items():
            complex_key = f'{k}.{inner_key}'
            differences.append(style_plain_list(complex_key,
                                                inner_val, differences))
