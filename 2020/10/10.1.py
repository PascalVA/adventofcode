#!/usr/bin/env python3

def parse_input(filepath):
    with open(filepath) as f:
        c = f.read().rstrip()

    return list(map(int, c.splitlines()))


adapters = parse_input('input.txt')
# adapters = parse_input('example.txt')

outlet, device_adapter = 0, max(adapters) + 3
adapters.extend([outlet, device_adapter])
adapters = sorted(adapters)

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

print(ones * threes)

# print(f"PART 1: {part1(numbers)}")
# print(f"PART 2: {part2(numbers, invalid)}")
