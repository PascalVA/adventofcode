#!/usr/bin/env python3

def read_input(filepath):
    with open(filepath) as f:
        content = f.read()

    lines = content.splitlines()
    for i, line in enumerate(lines):
        lines[i] = [x for x in line]

    return lines


def get_coordinate_value(area, x, y):
    """returns a coordinate value
       0: empty
       1: asteroid
    """
    return 1 if area[y][x] == '#' else 0


def get_asteroids_coordinates(area):
    """Returns the coordinates of all asteroids
       as a list of tuples: [(x, y), ...]

       e.g:
         [(0, 1), (0 ,4), (2, 0), ...]
    """
    asteroids = []
    for i, y in enumerate(area):
        for n, x in enumerate(y):
            if get_coordinate_value(area, n, i):
                asteroids.append((n, i))
    return asteroids


def get_slope(x_y, a_b):
    """Returns the slope of a line between two points
    >>> get_slope((0, 0), (1, 1))
    1.0
    >>> get_slope((0, 0), (2, 2))
    1.0
    >>> get_slope((0, 0), (1, 2))
    2.0
    >>> get_slope((0, 0), (2, 4))
    2.0
    >>> get_slope((-2, -4), (2, 4))
    2.0
    >>> get_slope((-10, 4), (2, 18))
    1.1666666666666667
    """
    delta_x = x_y[0] - a_b[0]
    delta_y = x_y[1] - a_b[1]

    if delta_x == 0:
        return 'undefined'

    return delta_y / delta_x


def visible_points_on_line(slope, origin, *args):
    """Returns the amount of visible points from origin on a line
       This can be either 0, 1 or 2.

       Origin and each point in *args must be on a straight line
    >>> visible_points_on_line(1.0, (0, 0), (-1, -1), (1, 1))
    2
    >>> visible_points_on_line(1.0, (0, 0), (-1, -1), (-2, -2))
    1
    >>> visible_points_on_line(1.0, (0, 0), (-1, -1), (-2, -2), (-5, -5))
    1
    >>> visible_points_on_line('undefined', (0, 0), (0, 1), (0, -1))
    2
    >>> visible_points_on_line('undefined', (0, 0), (0, -1), (0, -2))
    1
    """
    smaller = False
    larger = False
    if slope != 'undefined':
        for point in args:
            if point[0] < origin[0]:
                smaller = True
            if point[0] > origin[0]:
                larger = True
    else:
        for point in args:
            if point[1] < origin[1]:
                smaller = True
            if point[1] > origin[1]:
                larger = True

    return int(smaller) + int(larger)


def draw_area_values(area, results):
    for i, y in enumerate(area):
        _line = []
        for n, x in enumerate(y):
            key = ','.join(map(str, (n, i)))
            try:
                _line.append(str(results[key]['visible']))
            except KeyError:
                _line.append('.')
        print(''.join(_line))


area = read_input('input.txt')
# area = read_input('example1.txt')
# area = read_input('example2.txt')
# area = read_input('example3.txt')
# area = read_input('example4.txt')
asteroids = get_asteroids_coordinates(area)

results = {}
for asteroid in asteroids:
    key = ','.join(map(str, asteroid))
    result = results.setdefault(key, {})
    for _asteroid in asteroids:
        if asteroid == _asteroid:
            continue
        slope = get_slope(asteroid, _asteroid)

        slopes_points = result.setdefault(str(slope), [])
        slopes_points.append(_asteroid)

    visible = 0
    for slope, points in result.items():
        try:
            _slope = float(slope)
        except ValueError:
            _slope = slope

        visible += visible_points_on_line(slope, asteroid, *points)
    result['visible'] = visible

coord, result = sorted(results.items(), key=lambda i: i[1]['visible'])[-1]

draw_area_values(area, results)
print()

print(f'asteroid: {coord}')
print(f'result: {result["visible"]}')
