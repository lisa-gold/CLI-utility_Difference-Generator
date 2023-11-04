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


def build_plain_style(diff_dict, path=''):
    lines = []
    for k, v in diff_dict.items():
        new_path = f"{path}{v['key']}"
        v_new = convert_to_string(v['new_value'])
        v_old = convert_to_string(v['old_value'])
        if v['type'] == 'added':
            lines.append(f"Property '{new_path}' was added with value: {v_new}")
        if v['type'] == 'deleted':
            lines.append(f"Property '{new_path}' was removed")
        if v['type'] == 'updated':
            lines.append((f"Property '{new_path}' was updated. \
From {v_old} to {v_new}"))
        if v['type'] == 'nested':
            lines.append(build_plain_style(v["children"], f"{new_path}."))
    lines = list(filter(lambda x: x is not None and x != '', lines))
    return "\n".join(lines)
