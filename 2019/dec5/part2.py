#!/usr/bin/python
from operator import add, mul

with open('input.txt', 'r') as f:
    source = f.read().rstrip()
mem = [int(n) for n in source.split(',')]
#mem = [3,9,8,9,10,9,4,9,99,-1,8]  # eq 8 position mode
#mem = [3,9,7,9,10,9,4,9,99,-1,8]  # lt 8 position mode
#mem = [3,3,1108,-1,8,3,4,3,99]    # eq 8 immediate mode
#mem = [3,3,1107,-1,8,3,4,3,99]    # lt 8 immediate mode
#mem = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
#mem = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
#mem = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

inp = 5
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

    print(inst)

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
        mem[a] = inp
        shift = 2
        print("writing %d to position %d" % (inp, a))
    if op == 4:
        a = mem[ptr + 1]
        x = mem[a] if m1 == 0 else a
        shift = 2
        print(x)
    if op in [5,6]:
        a = mem[ptr + 1]
        b = mem[ptr + 2]
        x = mem[a] if m1 == 0 else a
        y = mem[b] if m2 == 0 else b
        # jump if true
        if op == 5 and x != 0:
            print("jump to %d" % y)
            ptr = y
            continue
        # jump if false
        if op == 6 and x == 0:
            print("jump to %d" % y)
            ptr = y
            continue
        shift = 3
    if op == 7:
        a = mem[ptr + 1]
        b = mem[ptr + 2]

        x = mem[a] if m1 == 0 else a
        y = mem[b] if m2 == 0 else b
        z = mem[ptr + 3]
        mem[z] = int(x < y)
        shift = 4
    if op == 8:
        a = mem[ptr + 1]
        b = mem[ptr + 2]

        x = mem[a] if m1 == 0 else a
        y = mem[b] if m2 == 0 else b
        z = mem[ptr + 3]
        mem[z] = int(x == y)
        shift = 4

    ptr += shift 
