#!/usr/bin/env python3
def parse_input(filepath):
    with open(filepath) as f:
        c = f.read().rstrip()
    return list(map(int, c.splitlines()))


def part1(numbers):
    for i1, n1 in enumerate(numbers):
        for i2, n2 in enumerate(numbers):
            if i1 == i2:
                continue
            if n1 + n2 == 2020:
                return(n1 * n2)


def part2(numbers):
    for i1, n1 in enumerate(numbers):
        for i2, n2 in enumerate(numbers):
            for i3, n3 in enumerate(numbers):
                if any([i1 == i2, i1 == i3, i2 == i3]):
                    continue
                if n1 + n2 + n3 == 2020:
                    return(n1 * n2 * n3)


numbers = parse_input('input.txt')

print("PART 1: " + str(part1(numbers)))
print("PART 2: " + str(part2(numbers)))
