# Formater - plain
def convert_to_string(value):
    if isinstance(value, dict):
        value_mod = '[complex value]'
    elif isinstance(value, bool):
        value_mod = str(value).lower()
    elif value is None:
        value_mod = 'null'
    elif not isinstance(value, str):
        value_mod = value
    else:
        value_mod = f"'{value}'"
    return value_mod


def build_plain_style(diff_dict):
    lines = []
    for k, v in diff_dict.items():
        v_new = convert_to_string(v['new_value'])
        v_old = convert_to_string(v['old_value'])
        if v['type'] == 'added':
            lines.append(f"Property '{v['key']}' was added with value: {v_new}")
        if v['type'] == 'deleted':
            lines.append(f"Property '{v['key']}' was removed")
        if v['type'] == 'updated':
            lines.append((f"Property '{v['key']}' was updated. \
From {v_old} to {v_new}"))
        if v['type'] == 'nested':
            diff_dict_nested = v["children"].copy()
            for inner_key, inner_value in diff_dict_nested.items():
                diff_dict_nested[inner_key]['key'] = '.'.join([v['key'],
                                                               inner_key])
            lines.append(build_plain_style(diff_dict_nested))
    lines = list(filter(lambda x: x is not None and x != '', lines))
    return "\n".join(lines)
