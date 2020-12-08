#!/usr/bin/env python3

def read_input(filepath):
    with open(filepath) as f:
        content = f.read()

    lines = content.splitlines()
    for i, line in enumerate(lines):
        op, arg = line.split(' ')
        lines[i] = (op, int(arg))

    return lines


def run(instructions):
    i, accumulator, indexes = 0, 0, []
    while i < len(instructions):
        if i in indexes:
            return False, accumulator

        inst, arg = instructions[i]

        if inst == 'acc':
            accumulator += arg
        if inst == 'jmp':
            i += arg
            continue

        indexes.append(i)
        i += 1

    return True, accumulator


# TODO: see if there is a better way to do this than brute-force
def part2(instructions):
    for i, _ in enumerate(instructions):
        _instructions = instructions[:]
        if instructions[i][0] in ['nop', 'jmp']:
            inst, arg = _instructions[i]
            _instructions[i] = (
                'nop' if inst == 'jmp' else 'jmp',
                arg
            )
            res, accumulator = run(_instructions)
            if res:
                return accumulator
    return None


instructions = read_input('input.txt')
# instructions = read_input('example.txt')

print(f"PART 1: {run(instructions)[1]}")
print(f"PART 2: {part2(instructions)}")
