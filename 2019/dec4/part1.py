#!/usr/bin/env python3

passrange = "134564-585159"

tests = [
    111111,
    223450,
    123789
]


def test_pass(n):
    adjacent = False
    decreasing = False
    prevchar = ""
    for char in str(n):
        if prevchar != "":
            if prevchar == char:
                adjacent = True
            if int(prevchar) > int(char):
                decreasing = True
        prevchar = char
    return adjacent and not decreasing


for test in tests:
    print(test, test_pass(test))


count = 0
for p in range(134564, 585159 + 1):
    if test_pass(p):
        count += 1

print(count)
