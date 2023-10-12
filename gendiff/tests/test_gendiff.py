import json
from gendiff.generate_diff_func import generate_diff
from gendiff.tests.fixtures.correct_results import (
    test_generate_diff_exp, test_generate_diff_the_same_file_exp,
    test_generate_diff_nested_exp, test_plain_style_exp)


ADDRESS = 'gendiff/tests/fixtures/'


def test_generate_diff(test_generate_diff_exp):
    # Check if function generate_diff works correctly
    diff = generate_diff(
        ADDRESS + 'flat1.json', ADDRESS + 'flat2.json')
    assert diff == test_generate_diff_exp


def test_generate_diff_the_same_file(test_generate_diff_the_same_file_exp):
    # Check if function generate_diff works with the same file
    diff = generate_diff(
        ADDRESS + 'flat1.json', ADDRESS + 'flat1.json')
    assert diff == test_generate_diff_the_same_file_exp


def test_generate_diff_yml(test_generate_diff_exp):
    # Check if function generate_diff works correctly
    diff = generate_diff(
        ADDRESS + 'flat1.yml', ADDRESS + 'flat2.json')
    assert diff == test_generate_diff_exp


def test_generate_diff_the_same_file_yml(test_generate_diff_the_same_file_exp):
    # Check if function generate_diff works with the same file
    diff = generate_diff(
        ADDRESS + 'flat1.yml', ADDRESS + 'flat1.yml')
    assert diff == test_generate_diff_the_same_file_exp


def test_generate_diff_nested(test_generate_diff_nested_exp):
    # Check if function works with nested
    diff = generate_diff(
        ADDRESS + 'file1.json', ADDRESS + 'file2.json')
    assert diff == test_generate_diff_nested_exp


def test_generate_diff_plain(test_plain_style_exp):
    diff = generate_diff(
        ADDRESS + 'file1.json', ADDRESS + 'file2.json',
        formatting='plain')
    assert diff == test_plain_style_exp


def test_generate_diff_json():
    # Check if function generate_diff works correctly
    diff = generate_diff(
        ADDRESS + 'file1.json', ADDRESS + 'file2.json', 'json')
    correct_res = json.load(open('gendiff/tests/fixtures/correct_result.json'))
    assert diff == correct_res
