#!/usr/bin/env python3

import sys

from copy import deepcopy
from functools import partial
from math import floor


TILE_MAP = {
    '.': 0,
    'L': 1,
    '#': 2,
    0: '.',
    1: 'L',
    2: '#',
    None: '*'
}


def parse_input(filepath):
    with open(filepath) as f:
        content = f.read()

    lines = content.splitlines()
    for i, line in enumerate(lines):
        lines[i] = [TILE_MAP[x] for x in line]

    return len(lines[0]), len(lines), flatten_list(lines)


def flatten_list(l):
    flat_list=[]
    for i in l:
        if isinstance(i, list):
            flat_list.extend(flatten_list(i))
            continue
        flat_list.append(i)
    return flat_list


def draw_area(w, area):
    sys.stdout.flush()
    output = '\r'
    for i, n in enumerate(area):
        if i % w == 0:
            output += '\n\r'
        output += TILE_MAP[n]
    output += '\n'
    sys.stdout.write(output)


def get_coord(w, area, x, y):
    index = y * w + x

    # handle out of bounds
    if x + 1 > w or x < 0:
        return None
    if 0 > index or index + 1 > len(area):
        return None

    return area[index]


def update_seat_part1(area, x, y):
    seat = get(area, x, y)

    directions = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (+1, 0),
        (-1, +1), (0, +1), (1, +1),
    ]
    occupied = 0
    for a, b in directions:
        result = get(area, x+a, y+b)
        if result == 2:
           occupied +=1

    if seat == 1 and occupied == 0:
        seat = 2
    if seat == 2 and occupied >= 4:
        seat = 1
    return seat


def update_seat_part2(area, x, y):
    seat = get(area, x, y)

    directions = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (+1, 0),
        (-1, +1), (0, +1), (1, +1),
    ]

    occupied = 0
    for dx, dy in directions:
        a, b = x, y
        result = 0
        while result == 0:
            a += dx
            b += dy
            result = get(area, a, b)
        if result == 2:
           occupied +=1

    if seat == 1 and occupied == 0:
        seat = 2
    if seat == 2 and occupied >= 5:
        seat = 1
    return seat


def run_round(w, area):
    new_area = deepcopy(area)
    for i, n in enumerate(area):
        x = i % w
        y = int(floor(i / w))
        new_area[i] = update_seat(area, x, y)
    return new_area


def solve(area):
    last = None
    while True:
        if area == last:
            break
    
        # draw(area)
        
        last = area[:]
        area = run(area)
    return area


width, height, area = parse_input('input.txt')
# width, height, area = parse_input('example.txt')

get = partial(get_coord, width)
draw = partial(draw_area, width)
run = partial(run_round, width)

update_seat = update_seat_part1
part1 = flatten_list(solve(area[:])).count(2)
update_seat = update_seat_part2
part2 = flatten_list(solve(area[:])).count(2)

print("PART1: " + str(part1))
print("PART2: " + str(part2))
