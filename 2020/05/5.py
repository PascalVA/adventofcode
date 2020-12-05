#!/usr/bin/env python3
def parse_input(filepath):
    with open(filepath) as f:
        c = f.read().rstrip()
    return c.splitlines()


def parse_seat(seat):
    # to binary
    s = seat.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    s = int(s, base=2)
    row = s >> 3
    column = int(bin(s)[-3:], base=2)
    return row * 8 + column


def part2(seats):
    all_seats = set(range(0, 1024))
    allocated = set([parse_seat(seat) for seat in seats])
    free_seats = all_seats - allocated
    # the first seat where the index does not match the value is our seat
    for i, v in enumerate(free_seats):
        if i != v:
            return v


seats = parse_input('input.txt')
# seats = parse_input('example.txt')

print("PART 1: " + str(max(map(parse_seat, seats))))
print("PART 2: " + str(part2(seats)))
