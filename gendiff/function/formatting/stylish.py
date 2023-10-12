from gendiff import generate_diff


def special_values(value):
    if value in [True, False]:
        new_value = str(value).lower()
    elif value is None:
        new_value = 'null'
    else:
        new_value = value
    return new_value


def sort_alph(diff_dict):
    keys_in_result = list(diff_dict.values())
    dict_joined = {}
    for elem in keys_in_result:
        dict_joined.update(elem)
    keys_in_result = list(dict_joined.keys())
    keys_in_result.sort()
    sorted_dict = {k: dict_joined[k] for k in keys_in_result}
    return sorted_dict


# Formater - stylish
def form_line(key, current_dict, symbol, level):
    bracket = '{'
    bracket_close = '}'
    line = ''
    if not isinstance(current_dict, dict):
        line += f'{"  " * level}{symbol} {key}: {current_dict}\n'
    else:
        line += f'{"  " * level}{symbol} {key}: {bracket}\n'
        level += 1
        for k, v in current_dict.items():
            line += form_line(k, v, ' ', level + 1)
        line += f'{"  " * level}{bracket_close}\n'
    return line


def style_inner_change(value, key, level):
    bracket = '{'
    bracket_close = '}'
    string = ''
    if not isinstance(value, dict):
        v_inner0 = special_values(value[0])
        v_inner1 = special_values(value[1])
        string += form_line(key, v_inner0, '-', level)
        string += form_line(key, v_inner1, '+', level)
    else:
        string += f'{"  " * level}  {key}: {bracket}\n'
        inner_style = style(value)[2:-2].replace('\n', f'\n{"  " * level}  ')
        string += (f'{"  " * level}  '
                   + inner_style + f'\n{"  " * level}  {bracket_close}\n')
    return string


def style(diff_dict):
    diff_dict_sorted = sort_alph(diff_dict)
    bracket_close = '}'
    string = '{\n'
    level = 1
    for k, val in diff_dict_sorted.items():
        v = special_values(val)
        if k in generate_diff.get_no_change(diff_dict).keys():
            string += form_line(k, v, ' ', level)
        if k in generate_diff.get_add(diff_dict).keys():
            string += form_line(k, v, '+', level)
        if k in generate_diff.get_sub(diff_dict).keys():
            string += form_line(k, v, '-', level)
        if k in generate_diff.get_inner_change(diff_dict).keys():
            string += style_inner_change(v, k, level)
    string += bracket_close
    return string
