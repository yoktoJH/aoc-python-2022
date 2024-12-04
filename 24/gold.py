from math import lcm
from collections import deque

walls = {(1, -1)}
winds = []
directions = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}


def move(wind):
    wind = wind.copy()
    x = wind["next"][0] + wind["direction"][0]
    y = wind["next"][1] + wind["direction"][1]
    wind["pos"] = wind["next"]
    if (x, y) in walls:
        if wind["direction"] == (1, 0):
            wind["next"] = (1, y)
        elif wind["direction"] == (-1, 0):
            wind["next"] = (width, y)
        elif wind["direction"] == (0, 1):
            wind["next"] = (x, 1)
        else:
            wind["next"] = (x, height)
    else:
        wind["next"] = (x, y)
    return wind


def make_next(wind):
    x = wind["pos"][0] + wind["direction"][0]
    y = wind["pos"][1] + wind["direction"][1]
    if (x, y) in walls:
        if wind["direction"] == (1, 0):
            wind["next"] = (1, y)
        elif wind["direction"] == (-1, 0):
            wind["next"] = (width, y)
        elif wind["direction"] == (0, 1):
            wind["next"] = (x, 1)
        else:
            wind["next"] = (x, height)
    else:
        wind["next"] = (x, y)


with open("vstup.txt") as vstup:
    for y, line in enumerate(vstup):
        sline = line.rstrip()
        for x, char in enumerate(sline):
            if char == "#":
                walls.add((x, y))
            elif char != ".":
                direction = directions[char]
                winds.append({"pos": (x, y), "next": (), "direction": direction})
    width = x - 1
    height = y - 1
    start = (1, 0)
    end = (x - 1, y)

for wind in winds:
    make_next(wind)

moves = [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]


def get_blocked(winds1):
    future_blocked = set()
    for wind in winds1:
        future_blocked.add(wind["next"])
    return future_blocked


blocked_arenas = []
for _ in range(lcm(width, height)):
    blocked_arenas.append(get_blocked(winds))
    next_winds = []
    for wind in winds:
        next_winds.append(move(wind))
    winds = next_winds

min_solution = 990
COCK_BLOCK = lcm(width, height)

reached = {start: 0}
queue = {start}
round = 0
print(start)
while end not in reached:
    new_queue = set()
    for place in queue:
        x, y = place
        for mx, my in moves:
            if (x + mx, y + my) not in blocked_arenas[round % COCK_BLOCK] and (x + mx, y + my) not in walls:
                if (x + mx, y + my) not in reached:
                    reached[(x + mx, y + my)] = round + 1
                new_queue.add((x + mx, y + my))
    queue = new_queue
    round += 1
print(round)
print("part1")
reached = {end: 0}
queue = {end}
while start not in reached:
    new_queue = set()
    for place in queue:
        x, y = place
        for mx, my in moves:
            if (x + mx, y + my) not in blocked_arenas[round % COCK_BLOCK] and (x + mx, y + my) not in walls:
                if (x + mx, y + my) not in reached:
                    reached[(x + mx, y + my)] = round + 1
                new_queue.add((x + mx, y + my))
    queue = new_queue
    round += 1
print(reached[start])
print("part2")
reached = {start: 0}
queue = {start}
while end not in reached:
    new_queue = set()
    for place in queue:
        x, y = place
        for mx, my in moves:
            if (x + mx, y + my) not in blocked_arenas[round % COCK_BLOCK] and (x + mx, y + my) not in walls:
                if (x + mx, y + my) not in reached:
                    reached[(x + mx, y + my)] = round + 1
                new_queue.add((x + mx, y + my))
    queue = new_queue
    round += 1
print(round)

