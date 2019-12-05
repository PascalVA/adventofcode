#!/usr/bin/python
from operator import add, mul

with open('input.txt', 'r') as f:
    source = f.read().rstrip()
mem = [int(n) for n in source.split(',')]


inp = 1
ptr = 0
opcodes = {
        1: add,
        2: mul,
}
while True:

    if ptr >= len(mem):
        break

    inst = "{:05}".format(mem[ptr])
    op = int(inst[3:5])
    m1 = int(inst[2])
    m2 = int(inst[1])
    m3 = int(inst[0])

    if op == 99:
        break

    if op in [1, 2]:
        a = mem[ptr + 1]
        b = mem[ptr + 2]

        x = mem[a] if m1 == 0 else a
        y = mem[b] if m2 == 0 else b
        z = mem[ptr + 3]
        mem[z] = opcodes[op](x, y)
        shift = 4
    if op == 3:
        a = mem[ptr + 1]
        mem[a] == inp
        shift = 2
    if op == 4:
        a = mem[ptr + 1]
        x = mem[a] if m1 == 0 else a
        print(x)
        shift = 2

    ptr += shift 
