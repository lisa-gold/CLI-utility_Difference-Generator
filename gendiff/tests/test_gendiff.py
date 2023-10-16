import os
import pytest
from gendiff.generate_diff_func import generate_diff


TESTS_DIR = os.path.dirname(os.path.abspath('gendiff/tests/test_gendiff'))
FIXTURE_PATH = f"{TESTS_DIR}/fixtures"


def build_path(file):
    path = FIXTURE_PATH + '/' + file
    return path


def open_file(file_path):
    with open(build_path(file_path)) as f:
        correct_result = f.read()
    return correct_result


@pytest.mark.parametrize("test_input, expected", [
    (generate_diff(build_path('flat1.json'), build_path('flat2.json')),
     open_file('correct_res_flat.txt')),
    (generate_diff(build_path('flat1.json'), build_path('flat1.json')),
     open_file('correct_res_the_same_file.txt')),
    (generate_diff(build_path('flat1.yml'), build_path('flat2.json')),
     open_file('correct_res_flat.txt')),
    (generate_diff(build_path('file1.json'), build_path('file2.json')),
     open_file('correct_res_nested.txt')),
    (generate_diff(build_path('file1.json'), build_path('file2.json'), 'plain'),
     open_file('correct_res_plain.txt')),
    (generate_diff(build_path('file1.json'), build_path('file2.json'), 'json'),
     open_file('correct_res.json'))
])
def test_generate_diff(test_input, expected):
    assert test_input == expected
