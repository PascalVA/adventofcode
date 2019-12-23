#!/usr/bin/python
from intcodecomp import IntcodeComp
from os import system

with open('input.txt', 'r') as f:
    source = f.read().rstrip()
program = [int(n) for n in source.split(',')]


def get_xy_index(x, y, width):
    return y * width + x


def draw_area(area, width, height):
    system("clear")
    output = ""
    for i, v in enumerate(area):
        if (i % width) == 0:
            output += "\n"
        output += {
            0: " ",
            1: "#",
            2: "+",
            3: "―",
            4: "•"
        }[v]
    print(output + "\n")


width, height = 38, 21
area = [0] * width * height

game = IntcodeComp([], program)
artifacts = []
o = False
while True:
    o = game.run()
    if o is True:
        break
    artifacts.append(o)
    #pos = get_xy_index(x, y)

i = 0
while i+2 <= len(artifacts):
    pos = get_xy_index(artifacts[i], artifacts[i+1], width)
    area[pos] = artifacts[i+2]
    i += 3


print(len(list(filter(lambda i: i == 2, area))))
#print(len(artifacts) / 3)
