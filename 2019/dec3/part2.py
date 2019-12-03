#!/usr/bin/python
import itertools, operator, re

tests = [
  {
      "result": 30,
      "source": [
          ["R8","U5","L5","D3"],
          ["U7","R6","D4","L4"]
      ]
  },
  {
      "result": 610,
      "source": [
          ["R75","D30","R83","U83","L12","D49","R71","U7","L72"],
          ["U62","R66","U55","R34","D71","R55","D58","R83"]
      ]
  },
  {
      "result": 410,
      "source": [
         ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"],
         ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]
      ]
  }
]


with open('input.txt', 'r') as f:
    source = f.read().rstrip()
source = [i.split(',') for i in source.split("\n")]


def intersect(l1, l2):
    return [i for i in l1 if i in l2]



def line_points(start, end):
    points = []
    sx, ex = (start[0], end[0])
    sy, ey = (start[1], end[1])

    if sx == ex:
        # y changed
        if sy < ey:
            points = list(itertools.product([sx], range(sy, ey+1)))
        else:
            points = list(reversed(
                list(itertools.product([sx], range(ey, sy+1)))
            ))
    if sy == ey:
        # x changed
        if sx < ex:
            points = list(itertools.product(range(sx, ex+1), [sy]))
        else:
            points = list(reversed(
                list(itertools.product(range(ex, sx+1), [sy]))
            ))

    return points


def move_pos(pos, path):
    direction, n = re.match('^([URDL])(\d+)$', path).groups()
    if direction == "U":
        f = operator.add
        x, y = 0, int(n)
    if direction == "D":
        f = operator.sub
        x, y = 0, int(n)
    if direction == "R":
        f = operator.add
        x, y = int(n), 0
    if direction == "L":
        f = operator.sub
        x, y = int(n), 0

    new_x = f(pos[0], x)
    new_y = f(pos[1], y)
    return ((new_x, new_y))


def solve(lines_paths):
    lines = []
    for line_paths in lines_paths:
        pos = (0, 0)  # x, y
        line = []

        for path in line_paths:
            new_pos = move_pos(pos, path)
            if not pos == new_pos:
                points = line_points(pos, new_pos)
                line.extend(points[1:])
            pos = new_pos
        lines.append(line)

    intersects = reduce(intersect, lines)

    steps = []
    for i in intersects:
        steps.append(lines[0].index(i) + lines[1].index(i) + 2)

    return min(steps)

for test in tests:
    result = solve(test["source"])
    if result == test["result"]:
        print("OK")
    else:
        print("NOK")

print(solve(source))
