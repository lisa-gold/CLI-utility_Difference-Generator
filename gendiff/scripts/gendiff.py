#!/usr/bin/env python3

from gendiff.parsing import parse
from gendiff import generate_diff


def main():
    args = parse()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
