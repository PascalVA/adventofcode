#!/usr/bin/python
import itertools
from intcodecomp import IntcodeComp

with open('input.txt', 'r') as f:
    source = f.read().rstrip()
program = [int(n) for n in source.split(',')]


def solve(program, phases):
    results = []
    a, b, c, d, e = phases
    amps = [
        IntcodeComp([a], program),
        IntcodeComp([b], program),
        IntcodeComp([c], program),
        IntcodeComp([d], program),
        IntcodeComp([e], program)
    ]
    
    o = 0
    while o is not True:
        for i, amp in enumerate(amps):
            o = amp.run([o])
            if o is True:
                return results[-1]
            if i == 4:
                results.append(o)

tests = [
    {
        "program": [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5],
        "phases":  [9, 8, 7, 6, 5],
        "expect":  139629729
    },
    {   
        "program": [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10],
        "phases":  [9, 7, 8, 5, 6],
        "expect":  18216
    }
]

for test in tests:
    print(solve(test["program"], test["phases"]))


results = []
for phases in itertools.permutations([5, 6, 7, 8, 9]):
    results.append(solve(program, phases))

print(max(results))
