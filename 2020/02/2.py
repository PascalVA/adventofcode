#!/usr/bin/env python3

from re import search as re_search

def parse_input(filepath):
    def parse_line(line):
        pattern = r'^(\d+)-(\d+)\s([a-z])\:\s(.*)'
        m = re_search(pattern, line).groups()
        return int(m[0]), int(m[1]), m[2], m[3]

    with open(filepath) as f:
        c = f.read().rstrip()

    return list(map(parse_line, c.splitlines()))


def validate1(password_obj):
    min_repeat, max_repeat, char, password = password_obj
    return min_repeat <= list(password).count(char) <= max_repeat


def validate2(password_obj):
    idx1, idx2, char, password = password_obj
    return [password[idx1-1], password[idx2-1]].count(char) == 1


passwords = parse_input('input.txt')
# passwords = parse_input('example.txt')

part1 = len(list(filter(validate1, passwords)))
part2 = len(list(filter(validate2, passwords)))

print(f"PART 1: {part1}")
print(f"PART 2: {part2}")
