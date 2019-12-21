#!/usr/bin/python
import itertools
from intcodecomp import IntcodeComp

with open('input.txt', 'r') as f:
    source = f.read().rstrip()
mem = [int(n) for n in source.split(',')]


program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
phases = [9, 8, 7, 6, 5]
expect = 139629729

program = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
phases = [9, 7, 8, 5, 6]
expect = 18216

results = []
#for i in itertools.permutations([5, 6, 7, 8, 9]):
#    results.append(test_settings(a,b,c,d,e))


a, b, c, d, e = [9, 8, 7, 6, 5]
results = []
A = IntcodeComp([a], mem)
B = IntcodeComp([b], mem)
C = IntcodeComp([c], mem)
D = IntcodeComp([d], mem)
E = IntcodeComp([e], mem)

o = 0
while True:
    o = A.run([o])
    if o is True:
        break
    print("A: %d" % (o,))

    o = B.run([o])
    if o is True:
        break
    print("B: %d" % (o,))

    o = C.run([o])
    if o is True:
        break
    print("C: %d" % (o,))

    o = D.run([o])
    if o is True:
        break
    print("D: %d" % (o,))

    o = E.run([o])
    if o is True:
        break
    print("E: %d" % (o,))

    results.append(o)

    from time import sleep
    sleep(1)


print(results)
