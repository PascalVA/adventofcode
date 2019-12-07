#!/usr/bin/python
filename = 'input.txt'
#filename = 'test2.txt'
with open(filename, 'r') as f:
    source = map(lambda s: s.strip(), f.readlines())

orbits = {}
for l in source:
    m, o = l.split(")")
    orbit = orbits.setdefault(m, [])
    orbit.append(o)


def get_parents(m, parents):
    parents.append(m)
    parent = [k for k in orbits if m in orbits[k]]
    if parent:
        get_parents(parent[0], parents)
    return parents


you = get_parents("YOU", [])
san = get_parents("SAN", [])
common_parent = [m for m in you if m in san][0]

print(you.index(common_parent) + san.index(common_parent) - 2)
