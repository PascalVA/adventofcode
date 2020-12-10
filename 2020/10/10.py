#!/usr/bin/env python3

from itertools import combinations
from math import prod


def parse_input(filepath):
    with open(filepath) as f:
        c = f.read().rstrip()

    return list(map(int, c.splitlines()))


def flatten_list(nested_list):
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(flatten_list(i))
            continue
        flat_list.append(i)
    return flat_list


def part1(adapters):
    ones = 0
    threes = 0
    for i, adapter in enumerate(adapters):
        difference = adapters[i] - adapters[i-1]
        if difference > 3:
            print("ERROR")
        if difference == 1:
            ones += 1
        if difference == 3:
            threes += 1

    return ones * threes


def find_compatible_adapters(adapters):
    compatability_map = {}
    for i, a1 in enumerate(adapters):
        cm = compatability_map.setdefault(a1, [])
        for a2 in adapters[i+1:]:
            if 3 >= (a2 - a1) >= 1:
                cm.append(a2)
    return compatability_map


def get_combinations(numbers):
    """Returns all possible combinations of the nubmers
       where the result size is larger than 1
    """
    result = []
    length = len(numbers)
    for i in range(0, length-1):
        result.append(list(combinations(numbers, length-i)))

    result = flatten_list(result)

    # combinations of a single pair only returns one tuple
    if len(result) == 1:
        result = result * 2

    return result


adapters = parse_input('input.txt')
# adapters = parse_input('example.txt')

outlet, device_adapter = 0, max(adapters) + 3
adapters.extend([outlet, device_adapter])
adapters = sorted(adapters)

# from pprint import pprint  # noqa: #402
# pprint(find_compatible_adapters(adapters))

results = []
seen = []
for adapter, comp in find_compatible_adapters(adapters).items():
    if len(comp) == 1:
        continue
    result = get_combinations(comp)
    if [r for r in result if r not in seen]:
        seen.extend(result)
        results.append(result)

print(prod(list(map(len, results))))

# 5 -> 6 -> 7
# 5 -> 7
# 6 -> 7
# 7

# 0:  [1],
# 1:  [4],
# 4:  [5, 6, 7],
# 5:  [6, 7],
# 6:  [7],
# 7:  [10],
# 10: [11, 12],
# 11: [12],
# 12: [15],
# 15: [16],
# 16: [19],
# 19: [22],
# 22: []

# print(f"PART 1: {part1(adapters)}")
# print(f"PART 2: {part2(numbers, invalid)}")
