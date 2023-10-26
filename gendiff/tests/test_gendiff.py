import os
import pytest
from gendiff.generate_diff_func import generate_diff


TESTS_DIR = os.path.dirname(os.path.abspath('gendiff/tests/test_gendiff'))
FIXTURE_PATH = f"{TESTS_DIR}/fixtures"


def build_path(file):
    return os.path.join(FIXTURE_PATH, file)


def get_content(file_path):
    with open(build_path(file_path)) as f:
        correct_result = f.read()
    return correct_result


@pytest.mark.parametrize("test_input1, test_input2, test_input3,expected", [
    (build_path('flat1.json'), build_path('flat2.json'), 'stylish',
     'correct_res_flat.txt'),
    (build_path('flat1.json'), build_path('flat1.json'), 'stylish',
     'correct_res_the_same_file.txt'),
    (build_path('flat1.yml'), build_path('flat2.json'), 'stylish',
     'correct_res_flat.txt'),
    (build_path('file1.json'), build_path('file2.json'), 'stylish',
     'correct_res_nested.txt'),
    (build_path('file1.json'), build_path('file2.json'), 'plain',
     'correct_res_plain.txt'),
    (build_path('file1.json'), build_path('file2.json'), 'json',
     'correct_res.json')
])
def test_generate_diff(test_input1, test_input2, test_input3, expected):
    assert generate_diff(test_input1, test_input2, test_input3) ==\
           get_content(expected)
