def transform_special_values(value):
    if isinstance(value, bool):
        new_value = str(value).lower()
    elif value is None:
        new_value = 'null'
    else:
        new_value = value
    return new_value


def build_stylish(diff_dict, level=0):
    result = []
    for key, v in diff_dict.items():
        curr_type = v.get('type')
        if curr_type == 'nested':
            level_inner = level + 1
            result.append(f'{"    " * (level + 1)}{key}: \
{build_stylish(v.get("children"),level_inner)}')
        if curr_type == 'same':
            result.extend(form_line(key, diff_dict[key]['new_value'],
                                    " ", level))
        if curr_type == 'added':
            result.extend(form_line(key, diff_dict[key]['new_value'],
                                    "+", level))
        if curr_type == 'deleted':
            result.extend(form_line(key, diff_dict[key]['old_value'],
                                    "-", level))
        if curr_type == 'updated':
            result.extend(form_line_update(key, level, diff_dict))
    result.insert(0, '{')
    result.append(f'{"    " * level}' + '}')
    return "\n".join(result)


def form_line(key, value, symbol, level):
    line = []
    bracket = '{'
    bracket_close = '}'
    value = transform_special_values(value)
    if not isinstance(value, dict):
        line.append(f'{"    " * level}  {symbol} {key}: {value}')
    else:
        line.append(f'{"    " * level}  {symbol} {key}: {bracket}')
        inner_level = level + 1
        for k, v in value.items():
            line.extend(form_line(k, v, ' ', inner_level))
        line.append(f'{"    " * inner_level}{bracket_close}')
    return line


def form_line_update(key, level, diff_dict):
    lines = []
    lines.extend(form_line(key, diff_dict[key]['old_value'], "-", level))
    lines.extend(form_line(key, diff_dict[key]['new_value'], "+", level))
    return lines
