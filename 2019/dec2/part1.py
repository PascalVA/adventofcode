#!/usr/bin/python
with open('input.txt', 'r') as f:
    source = f.read().rstrip()

init = [int(n) for n in source.split(',')]
init[1], init[2] = (12, 2)


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


ptr = 0
while True:

    if ptr >= len(init) or init[ptr] == 99:
        break

    x = init[ptr + 1]
    y = init[ptr + 2]
    z = init[ptr + 3]

    if init[ptr] == 1:
        init[z] = add(init[x], init[y])
    if init[ptr] == 2:
        init[z] = mul(init[x], init[y])

    ptr += 4

print(init[0])
