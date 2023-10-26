from gendiff.formatters import stylish


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


def build_plain_style(diff_dict):
    return build_plain_result(diff_dict)


def build_plain_result(diff_dict):
    differences = []
    for k, val in diff_dict.items():
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
            build_plain_nested(k, val["children"][0], differences)
    differences = list(filter(lambda x: x is not None and x != '', differences))
    return "\n".join(differences)


def build_plain_nested(k, diff_dict_nested, differences):
    for inner_key, inner_val in diff_dict_nested.items():
        complex_key = '.'.join([k, inner_key])
        differences.append(build_plain_result({complex_key: inner_val}))
