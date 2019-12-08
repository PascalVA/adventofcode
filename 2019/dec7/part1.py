#!/usr/bin/python
import itertools
from intcodecomp import IntcodeComp

with open('input.txt', 'r') as f:
    source = f.read().rstrip()
mem = [int(n) for n in source.split(',')]


def validate_phases(l):
    return len(set(l)) == 5


def test_settings(a, b, c, d, e):
    A = IntcodeComp([a, 0], mem).run()
    B = IntcodeComp([b, A], mem).run()
    C = IntcodeComp([c, B], mem).run()
    D = IntcodeComp([d, C], mem).run()
    E = IntcodeComp([e, D], mem).run()
    return E

results = []
for i in range(0, 100000):
    n = ("{:05d}".format(i))
    l = [int(c) for c in n if int(c) <= 4]
    if not validate_phases(l):
        continue
    a,b,c,d,e = l
    results.append(test_settings(a,b,c,d,e))

print(max(results))
