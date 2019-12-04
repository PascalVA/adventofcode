#!/usr/bin/python
import itertools

EXPECTED = 19690720

with open('input.txt', 'r') as f:
    source = f.read().rstrip()

init = [int(n) for n in source.split(',')]


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


for n, v in itertools.product(range(0,100), range(0,100)):
    mem = init[:]  # copy values
    mem[1], mem[2] = n, v
    ptr = 0

    while True:
        try:
            if ptr >= len(mem) or mem[ptr] == 99:
                break

            x = mem[ptr + 1]
            y = mem[ptr + 2]
            z = mem[ptr + 3]

            if mem[ptr] == 1:
                mem[z] = add(mem[x], mem[y])
            if mem[ptr] == 2:
                mem[z] = mul(mem[x], mem[y])

            ptr += 4
        except:
            break

    if mem[0] == EXPECTED:
        break

print(mem[1] * 100 + mem[2])
