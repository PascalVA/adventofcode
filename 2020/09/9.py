#!/usr/bin/env python3

def parse_input(filepath):
    with open(filepath) as f:
        c = f.read().rstrip()

    return list(map( int, c.splitlines()))


def find_contiguous_sum(numbers, expected):
    r = 0
    while r < expected:
        for i, n in enumerate(numbers):
            r += n
            if r == expected:
                return numbers[:i+1]
    return None


# TODO: this can be improved (same for day 1) 
def check_add_result(numbers, result):
    results = []
    for i1, n1 in enumerate(numbers):
        for i2, n2 in enumerate(numbers):
            if i1 == i2:
                continue
            if n1 + n2 == result:
                results.append((n1, n2))
    return results, result


def part1(numbers):
    i = PREAMBLE
    while i < len(numbers):
        results, result = check_add_result(
            numbers[i-PREAMBLE:i],
            numbers[i]
        )
        if not results:
            return result
        i += 1


def part2(numbers, invalid):
    i = 0
    while i < len(numbers):
        result = find_contiguous_sum(numbers[i:], invalid)
        if result:
            return min(result[:i+1]) + max(result[:i+1])
        i += 1


PREAMBLE=25
numbers = parse_input('input.txt')
invalid = 373803594 

# PREAMBLE=5
# numbers = parse_input('example.txt')
# invalid = 127

print(f"PART 1: {part1(numbers)}")
print(f"PART 2: {part2(numbers, invalid)}")
