#!/usr/bin/env python3

import re


def parse_input(filepath):
    def parse_line(line):
        a, b = re.search(r'^([A-Z])(\d+)', line).groups()
        return a, int(b)

    with open(filepath) as f:
        content = f.read()

    return [parse_line(l) for l in content.splitlines()]


class Boat1(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        self.direction_names = ['N', 'E', 'S', 'W']
        self.directions = [(0, -1), (1, 0), (0, +1), (-1, 0)]
        self.direction = 1  # index of directions

    def parse_instruction(self, instruction):
        op, n = instruction
        if op == 'F':
            self.forward(int(n))
        elif op in ['L', 'R']:
            self.turn(*instruction)
        else:
            self.move(op, int(n)) 

    def move(self, d, n):
        index = self.direction_names.index(d)
        a, b = self.directions[index]
        self.x += a*n 
        self.y += b*n

    def forward(self, n):
        a, b = self.directions[self.direction]
        self.x += a*n 
        self.y += b*n

    def turn(self, d, degrees):
        shift = int(degrees / 90)
        if d == 'L':
            shift = 0 - shift

        # degrees are only increments of 90
        self.direction = (
                self.direction + shift
            ) % len(self.directions)


class Boat2(object):
    def __init__(self, x=0, y=0, waypoint=None):
        self.direction = 1  # index of directions
        self.x = x
        self.y = y

        if waypoint:
            self.waypoint = waypoint
        else:
            self.waypoint = Waypoint()

    def parse_instruction(self, instruction):
        op, n = instruction
        if op == 'F':
            a, b = self.waypoint.x, self.waypoint.y
            self.x += a*n 
            self.y += b*n
        elif op in ['R', 'L']:
            self.waypoint.rotate(op, n)
        else:
            self.waypoint.move(op, n) 


class Waypoint(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, d, n):
        a, b = {
           'N': (0, -1),
           'E': (1, 0),
           'S': (0, +1),
           'W': (-1, 0)
        }[d]

        self.x += a*n 
        self.y += b*n

    def rotate(self, d, n):
        def invert(n):
            return (0 - n) if n > 0 else abs(n)

        def rotate_90(d):
            if d == 'R':
                # 10, -4 rotates to 4, -10
                x, y = self.x, self.y
                self.x, self.y = invert(y), x
            else:
                # 10, -4 rotates to 10, -4
                x, y = self.x, self.y
                self.x, self.y = y, invert(x)

        count = int(n / 90)
        for i in range(count):
            rotate_90(d)


def solve(b, instructions):
    for i in instructions:
        b.parse_instruction(i)
    return abs(b.x) + abs(b.y)


if __name__ == '__main__':
    instructions = parse_input('input.txt')
    # instructions = parse_input('example.txt')

    print("PART 1: " + str(solve(Boat1(), instructions)))
    print("PART 2: " + str(solve(Boat2(waypoint=Waypoint(10, -1)), instructions)))
