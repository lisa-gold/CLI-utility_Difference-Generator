from gendiff import generate_diff_func
from gendiff.function.formatting import stylish


def inner_style(key, inner_dict, file_json):
    if not isinstance(inner_dict, dict):
        temp_dict1 = {f'-{key}': inner_dict[0]}
        temp_dict2 = {f'+{key}': inner_dict[1]}
        file_json.update(temp_dict1)
        file_json.update(temp_dict2)
    else:
        file_json[key] = style_json(inner_dict)


def style_json(diff_dict):
    file_json = {}
    sorted_dict = stylish.sort_alph(diff_dict)
    for k, v in sorted_dict.items():
        if k in generate_diff_func.get_no_change(diff_dict).keys():
            file_json.update({k: v})
        if k in generate_diff_func.get_add(diff_dict).keys():
            temp_dict = {f'+{k}': v}
            file_json.update(temp_dict)
        if k in generate_diff_func.get_sub(diff_dict).keys():
            temp_dict = {f'-{k}': v}
            file_json.update(temp_dict)
        if k in generate_diff_func.get_inner_change(diff_dict).keys():
            inner_style(k, v, file_json)
    return str(file_json)
