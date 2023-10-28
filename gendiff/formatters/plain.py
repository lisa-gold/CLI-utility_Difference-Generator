# Formater - plain
def transform_special_values(value):
    if isinstance(value, bool):
        new_value = str(value).lower()
    elif value is None:
        new_value = 'null'
    else:
        new_value = value
    return new_value


def modify_according_to_type(value):
    if isinstance(value, dict):
        value_mod = '[complex value]'
    elif value in [True, False]:
        value_mod = str(value).lower()
    elif value is None:
        value_mod = 'null'
    elif not isinstance(value, str):
        value_mod = value
    else:
        value_mod = f"'{value}'"
    return value_mod


def build_plain_style(diff_dict):
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
            diff_dict_nested = val["children"].copy()
            for inner_key in list(val["children"].keys()):
                complex_key = '.'.join([k, inner_key])
                diff_dict_nested[complex_key] = diff_dict_nested.pop(inner_key)
            differences.append(build_plain_style(diff_dict_nested))
    differences = list(filter(lambda x: x is not None and x != '', differences))
    return "\n".join(differences)
