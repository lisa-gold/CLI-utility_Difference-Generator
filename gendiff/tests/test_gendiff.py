from gendiff.generate_diff_func import generate_diff


ADDRESS = 'gendiff/tests/fixtures/'


def test_generate_diff():
    # Check if function generate_diff works correctly
    diff = generate_diff(
        ADDRESS + 'flat1.json', ADDRESS + 'flat2.json')
    with open(ADDRESS + 'correct_res_flat.txt') as f:
        test_generate_diff_exp = f.read()
    assert diff == test_generate_diff_exp


def test_generate_diff_the_same_file():
    # Check if function generate_diff works with the same file
    diff = generate_diff(
        ADDRESS + 'flat1.json', ADDRESS + 'flat1.json')
    with open(ADDRESS + 'correct_res_the_same_file.txt') as f:
        test_generate_diff_the_same_file_exp = f.read()
    assert diff == test_generate_diff_the_same_file_exp


def test_generate_diff_yml():
    # Check if function generate_diff works correctly
    diff = generate_diff(
        ADDRESS + 'flat1.yml', ADDRESS + 'flat2.json')
    with open(ADDRESS + 'correct_res_flat.txt') as f:
        test_generate_diff_exp = f.read()
    assert diff == test_generate_diff_exp


def test_generate_diff_the_same_file_yml():
    # Check if function generate_diff works with the same file
    diff = generate_diff(
        ADDRESS + 'flat1.yml', ADDRESS + 'flat1.yml')
    with open(ADDRESS + 'correct_res_the_same_file.txt') as f:
        test_generate_diff_the_same_file_exp = f.read()
    assert diff == test_generate_diff_the_same_file_exp


def test_generate_diff_nested():
    # Check if function works with nested
    diff = generate_diff(
        ADDRESS + 'file1.json', ADDRESS + 'file2.json')
    with open(ADDRESS + 'correct_res_nested.txt') as f:
        test_generate_diff_nested_exp = f.read()
    assert diff == test_generate_diff_nested_exp


def test_generate_diff_plain():
    diff = generate_diff(
        ADDRESS + 'file1.json', ADDRESS + 'file2.json',
        formatting='plain')
    with open(ADDRESS + 'correct_res_plain.txt') as f:
        test_plain_style_exp = f.read()
    assert diff == test_plain_style_exp


def test_generate_diff_json():
    # Check if function generate_diff works correctly
    diff = generate_diff(
        ADDRESS + 'file1.json', ADDRESS + 'file2.json', 'json')
    with open(ADDRESS + 'correct_res.json') as f:
        test_json_style_exp = f.read()
    assert diff == test_json_style_exp
