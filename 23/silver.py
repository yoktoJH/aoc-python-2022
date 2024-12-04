import math

elves = set()
with open("vstup.txt") as vstup:
    for y, line in enumerate(vstup):
        sline = line.rstrip()
        for x, char in enumerate(sline):
            if char == "#":
                elves.add((x, y))

around = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
logic = ["N", "S", "W", "E"]
heading_checks = {"N": [(-1, -1), (0, -1), (1, -1)], "S": [(-1, 1), (0, 1), (1, 1)], "W": [(-1, -1), (-1, 0), (-1, 1)],
                  "E": [(1, -1), (1, 0), (1, 1)]}
for _ in range(10):
    moves = {}
    for elf in elves:
        x, y = elf
        move = False
        for dx, dy in around:
            if (x + dx, y + dy) in elves:
                move = True
                break
        if not move:
            continue
        for direction in logic:
            empty = True
            for nx, ny in heading_checks[direction]:
                if (x + nx, y + ny) in elves:
                    empty = False
                    break
            if empty:
                nx, ny = heading_checks[direction][1]
                final_pos = (x + nx, y + ny)
                e = moves.get(final_pos, [])
                e.append(elf)
                moves[final_pos] = e
                break
    # now we know where everyone wants to go, so we make moves
    for pos in moves:
        if len(moves[pos]) == 1:
            elves.remove(moves[pos][0])
            elves.add(pos)
    logic.append(logic.pop(0))

max_x = -math.inf
min_x = math.inf
max_y = -math.inf
min_y = math.inf
for x, y in elves:
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y

print((abs(max_x - min_x)+1)*(abs(max_y-min_y)+1)-len(elves))