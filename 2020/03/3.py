#!/usr/bin/env python3
from math import prod

def read_input(filepath):
    with open(filepath) as f:
        content = f.read()

    lines = content.splitlines()
    for i, line in enumerate(lines):
        lines[i] = [x for x in line]

    return lines


def get_coordinate_value(area, x, y):
    """returns a coordinate value
       0: empty
       1: tree
    """
    return 1 if area[y][x] == '#' else 0


def solve(area, x_offset, y_offset):
    w, h = len(area[0]), len(area)
    count, x, y = 0, 0, 0
    while True:
        if get_coordinate_value(area, x, y):
            count += 1
        x = (x + x_offset) % w
        y = y + y_offset
        if y > h - 1:
            break
    return count


area = read_input('input.txt')
# area = read_input('example.txt')

part1 = solve(area, 3, 1)
offsets = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
part2 = prod([solve(area, x, y) for x, y in offsets])

print(f"PART 1: {part1}")
print(f"PART 2: {part2}")
