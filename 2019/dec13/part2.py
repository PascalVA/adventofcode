#!/usr/bin/env python3
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


def play_game(joy_input, program):
    # Setup play field
    width, height = 38, 21
    area = [0] * width * height

    # load game with joy input
    game = IntcodeComp(joy_input, program)

    solved = False
    scores = [0]  # score history
    bidxs = []  # ball indexes
    pidxs = []  # paddle indexes

    while True:
        # wait for screen to initialize
        if 3 in area and 4 in area:

            draw_area(area, width, height)
            print("[ %d ]" % (scores[0],))

            if not 2 in area:
                solved = True

            bidxs.append(area.index(4) % width)
            bidxs = bidxs[-4:]
            pidxs.append(area.index(3) % width)
            pidxs = pidxs[-4:]

        # one program cycle
        x = game.run()
        if x is True:
            if solved:
                return True, scores[0]
            else:
                return False, (len(joy_input), bidxs[0], pidxs[0], scores[0])
        y = game.run()
        if y is True:
            if solved:
                return True, scores[0]
            else:
                return False, (len(joy_input), bidxs[0], pidxs[0], scores[0])
        z = game.run()
        if z is True:
            if solved:
                return True, scores[0]
            else:
                return False, (len(joy_input), bidxs[0], pidxs[0], scores[0])

        # condition for score update
        if x == -1 and y == 0:
            scores.append(z)
            scores = scores[-1:]
            continue

        # regular screen output
        pos = get_xy_index(x, y, width)
        area[pos] = z

# Insert coins
program[0] = 2

# initial joypad input
#joy_input = [0] * 10000

# Solution after 67 games played
with open('joyinput.txt', 'r') as f:
    source = f.read().rstrip()
joy_input = [int(n) for n in source.split(',')]

# Play game until you win
offsets = []
fails = []
games = 0

while True:
    #TODO: The program should not be ran from start each time
    #      but rather pick up from the last index
    exit, result = play_game(joy_input[:], program)

    if exit == False:
        position, bidx, pidx, score = result
        # move paddle towards ball
        if bidx > pidx:
            # ball to the right of paddle
            distance = bidx - pidx
            inputval = 1
        else:
            # ball to the left of paddle
            distance = pidx - bidx
            inputval = -1

        offset = len(joy_input) - position - distance
        for i in range(offset, offset + distance):
            joy_input[i-1] = inputval

        if len(offsets) >= 3 and len(set(offsets[-3:])) == 1:
            print("NO MORE IMPROVEMENT")
            for fail in fails:
                print(fail)
            break
        offsets.append(offset)

        fails.append("* position: %d, ball: %d, paddle: %d, distance: %d, score: %d"
                         % (position,
                            bidx,
                            pidx,
                            distance,
                            score)
        )
    else:
        break
