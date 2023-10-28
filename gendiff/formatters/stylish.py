def transform_special_values(value):
    if isinstance(value, bool):
        new_value = str(value).lower()
    elif value is None:
        new_value = 'null'
    else:
        new_value = value
    return new_value


def build_stylish(diff_dict):
    level = 1
    lines = build_inner(diff_dict, level)
    return '{\n' + "\n".join(lines) + '\n}'


def build_inner(diff_dict, level):
    line = []
    keys = list(diff_dict.keys())
    for key in keys:
        line.append(match_type(key, diff_dict, level))
    return line


def match_type(key, diff_dict, level):
    string = ''
    match diff_dict[key]['type']:
        case 'same':
            string += form_line(key, diff_dict[key]['new_value'], " ", level)
        case 'added':
            string += form_line(key, diff_dict[key]['new_value'], "+", level)
        case 'deleted':
            string += form_line(key, diff_dict[key]['old_value'], "-", level)
        case 'updated':
            string += form_line_update(key, level, diff_dict)
        case 'nested':
            string += form_line_nested(key, level, diff_dict)
    return string


def form_line(key, value, symbol, level):
    line = []
    bracket = '{'
    bracket_close = '}'
    value = transform_special_values(value)
    if not isinstance(value, dict):
        line.append(f'{"  " * level}{symbol} {key}: {value}')
    else:
        line.append(f'{"  " * level}{symbol} {key}: {bracket}')
        level += 1
        for k, v in value.items():
            line.append(form_line(k, v, ' ', level + 1))
        line.append(f'{"  " * level}{bracket_close}')
    return '\n'.join(line)


def form_line_update(key, level, diff_dict):
    lines = []
    lines.append(form_line(key, diff_dict[key]['old_value'], "-", level))
    lines.append(form_line(key, diff_dict[key]['new_value'], "+", level))
    return '\n'.join(lines)


def form_line_nested(key, level, diff_dict):
    line = []
    bracket = '{'
    bracket_close = '}'
    children = diff_dict[key]['children']
    line.append(f'{"  " * level}  {key}: {bracket}')
    level += 1
    line.append('\n'.join(build_inner(children, level + 1)))
    line.append(f'{"  " * level}{bracket_close}')
    return '\n'.join(line)
