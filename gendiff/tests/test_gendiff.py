import os
import pytest
from gendiff.gendiff import generate_diff


TESTS_DIR = os.path.dirname(os.path.abspath('gendiff/tests/test_gendiff'))
FIXTURE_PATH = f"{TESTS_DIR}/fixtures"


def generate_fixture_path(file):
    return os.path.join(FIXTURE_PATH, file)


def get_content(file_path):
    with open(generate_fixture_path(file_path)) as f:
        correct_result = f.read()
    return correct_result


@pytest.mark.parametrize("test_input1, test_input2, test_input3,expected", [
    ('flat1.json', 'flat2.json', 'stylish', 'correct_res_flat.txt'),
    ('flat1.json', 'flat1.json', 'stylish', 'correct_res_the_same_file.txt'),
    ('flat1.yml', 'flat2.json', 'stylish', 'correct_res_flat.txt'),
    ('file1.json', 'file2.json', 'stylish', 'correct_res_nested.txt'),
    ('file1.json', 'file2.json', 'plain', 'correct_res_plain.txt'),
    ('file1.json', 'file2.json', 'json', 'correct_res.json')
])
def test_generate_diff(test_input1, test_input2, test_input3, expected):
    assert generate_diff(generate_fixture_path(test_input1),
           generate_fixture_path(test_input2), test_input3) ==\
           get_content(expected)
