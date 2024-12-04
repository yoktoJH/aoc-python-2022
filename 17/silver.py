with open("vstup.txt") as vstup:
    for line in vstup:
        air_currents = line.rstrip()
print(len(air_currents))
chamber = [0 for i in range(7)]
line = [(0, 0), (1, 0), (2, 0), (3, 0)]
plus = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
an_l = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
stlp = [(0, 0), (0, 1), (0, 2), (0, 3)]
square = [(0, 0), (0, 1), (1, 0), (1, 1)]
shapes = [line, plus, an_l, stlp, square]


def make_shape(i, max_height):
    x = 2
    y = max_height + 4
    new_shape = []
    for bx, by in shapes[i]:
        new_shape.append((x + bx, y + by))
    return new_shape


def movement_direction(i):
    if air_currents[i] == ">":
        return 1
    return -1


def move_shape_side(shape, direction):
    new_shape = []
    for x, y in shape:
        if 0 <= x + direction < 7 and (x + direction, y) not in stuck_rocks:
            new_shape.append((x + direction, y))
        else:
            return shape
    return new_shape


def move_shape_down(shape):
    new_shape = []
    for x, y in shape:
        if y - 1 != 0 and (x, y - 1) not in stuck_rocks:
            new_shape.append((x, y - 1))
        else:
            for x, y in shape:
                if chamber[x] < y:
                    chamber[x] = y
                stuck_rocks.add((x, y))
            return []
    return new_shape



shape_i = 0
wind_i = 0
stuck_rocks = set()
for i in range(2022):
    shape = make_shape(shape_i, max(chamber))
    shape_i = (shape_i + 1) % len(shapes)
    while shape:
        shape = move_shape_side(shape, movement_direction(wind_i))
        wind_i = (wind_i + 1) % len(air_currents)
        shape = move_shape_down(shape)
print(wind_i)
print(max(chamber))
