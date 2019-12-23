#!/usr/bin/python
import itertools
from os import system
from math import floor
from intcodecomp import IntcodeComp

import sys
from time import sleep

with open('input.txt', 'r') as f:
    source = f.read().rstrip()
program = [int(n) for n in source.split(',')]


class Robot(object):

    def __init__(self, program, width, height):

        self.painted = set()

        self.height = height
        self.width = width

        # 0 is black, 1 is white
        self.area = [0] * width * height

        # The robot should start in the middle of the area
        self.position = int(floor(width * height / 2) - width / 2 - 1)

        self.area[self.position] = 1

        # 0 up, 1 right, 2 down, 3 left
        self.direction = 0

        self.program = IntcodeComp([], program)

    def up(self):
        self.position = self.position - self.width

    def right(self):
        self.position = self.position + 1

    def down(self):
        self.position = self.position + self.width

    def left(self):
        self.position = self.position - 1

    def __get_xy_index(self, x, y):
        return (self.width * y) + x

    def draw_area(self):
        system("clear")
        draw = ""
        for i, v in enumerate(self.area):
            if (i % self.width) == 0:
                draw += "\n"
            if i == self.position:
                draw += {
                    0: "^",
                    1: ">",
                    2: "<",
                    3: "v"
                }[self.direction]
            elif v == 0:
                draw += "."
            else:
                draw += "#"
        print(draw)

    def turn(self, direction):
        if direction == 0:
            self.direction -= 1  # left
        else:
            self.direction += 1  # right

        if self.direction < 0:
            self.direction = 3
        if self.direction > 3:
            self.direction = 0

    def move(self):
        """move one step in <direction>"""
        {
            0: self.up,
            1: self.right,
            2: self.down,
            3: self.left
        }[self.direction]()

    def run(self):
        o = False
        while True:
            o = self.program.run([self.area[self.position]])
            if o is True:
                break
            self.area[self.position] = o  # paint

            o = self.program.run()
            if o is True:
                break

            self.turn(o)
            self.move()

            self.painted.add(self.position)
        self.draw_area()
        return self.painted

Robot(program, 100, 100).run()
