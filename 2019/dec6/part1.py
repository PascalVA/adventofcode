#!/usr/bin/python
filename = 'input.txt'
#filename = 'test1.txt'
with open(filename, 'r') as f:
    source = map(lambda s: s.strip(), f.readlines())

orbits = {}
for l in source:
    m, o = l.split(")")
    orbit = orbits.setdefault(m, [])
    orbit.append(o)


def get_children(m):
    global res
    for c in orbits.get(m, []):
        res = get_children(c)
        res += 1
    return res


res = 0
for mass in orbits:
    res = get_children(mass)

print(res)
