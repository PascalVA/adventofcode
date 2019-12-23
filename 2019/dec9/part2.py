#!/usr/bin/python
import itertools
from intcodecomp import IntcodeComp

with open('input.txt', 'r') as f:
    source = f.read().rstrip()
program = [int(n) for n in source.split(',')]


def solve(program, inputs):
    prog = IntcodeComp(inputs, program)
    results = []
    o = False
    while True:
        o = prog.run()
        if o is True:
            break
        results.append(o)

    return results


print(solve(program, [2]))
