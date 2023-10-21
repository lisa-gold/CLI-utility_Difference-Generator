def transform_special_values(value):
    if value in [True, False]:
        new_value = str(value).lower()
    elif value is None:
        new_value = 'null'
    else:
        new_value = value
    return new_value


def style(diff_dict):
    string = '{\n'
    bracket_close = '}'
    level = 1
    string += style_inner(diff_dict, level)
    string += bracket_close
    return string


def style_inner(diff_dict, level):
    string = ''
    keys = list(diff_dict.keys())
    for key in keys:
        if diff_dict[key]['type'] == 'same':
            string += form_line(key, diff_dict[key]['new_value'], " ", level)
        if diff_dict[key]['type'] == 'added':
            string += form_line(key, diff_dict[key]['new_value'], "+", level)
        if diff_dict[key]['type'] == 'deleted':
            string += form_line(key, diff_dict[key]['old_value'], "-", level)
        if diff_dict[key]['type'] == 'updated':
            string += form_line_update(key, level, diff_dict)
    return string


def form_line(key, value, symbol, level):
    line = ''
    bracket = '{'
    bracket_close = '}'
    value = transform_special_values(value)
    if not isinstance(value, dict):
        line += f'{"  " * level}{symbol} {key}: {value}\n'
    else:
        line += f'{"  " * level}{symbol} {key}: {bracket}\n'
        level += 1
        for k, v in value.items():
            line += form_line(k, v, ' ', level + 1)
        line += f'{"  " * level}{bracket_close}\n'
    return line


def form_line_update(key, level, diff_dict):
    line = ''
    bracket = '{'
    bracket_close = '}'
    if isinstance(diff_dict[key]['old_value'], dict) and\
       isinstance(diff_dict[key]['new_value'], dict):
        children = diff_dict[key]['children'][0]
        line += f'{"  " * level}  {key}: {bracket}\n'
        level += 1
        line += style_inner(children, level + 1)
        line += f'{"  " * level}{bracket_close}\n'
    else:
        line += form_line(key, diff_dict[key]['old_value'], "-", level)
        line += form_line(key, diff_dict[key]['new_value'], "+", level)
    return line
