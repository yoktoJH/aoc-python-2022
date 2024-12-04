from collections import deque

with open("vstup.txt") as vstup:
    bricks = set()
    for line in vstup:
        x, y, z = line.rstrip().split(",")
        x = int(x)
        y = int(y)
        z = int(z)
        bricks.add((x, y, z))

sides = 0
flooded = set()
queue = deque([(0, 0, 0)])
while queue:
    x, y, z = queue.popleft()
    if (x, y, z) not in flooded:
        for sx, sy, sz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            if (x + sx, y + sy, z + sz) in bricks:
                sides += 1
            elif (x + sx, y + sy, z + sz) not in flooded and -4 <= (x + sx) < 25 and -4 <= (y + sy) < 25 and -4 <= (
                    z + sz) < 25:
                queue.append((x + sx, y + sy, z + sz))
    flooded.add((x, y, z))
print(sides)
