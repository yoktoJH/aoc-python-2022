with open("vstup.txt") as vstup:
    empty = set()

    for line in vstup:
        #print(line)
        removed = set()
        sline = line.rstrip().replace(",", "").replace(":", "").split(" ")
        sx = int(sline[2][2:])
        sy = int(sline[3][2:])
        bx = int(sline[8][2:])
        by = int(sline[9][2:])
        distance = abs(sx - bx) + abs(sy - by) + 1
        for x, y in empty:
            if abs(sx - x) + abs(sy - y) < distance:
                removed.add((x,y))
        empty.difference_update(removed)
        removed = set()
        x = sx - distance
        while x <= sx + distance:
            empty.add((x, sy - distance + abs(sx - x)))
            empty.add((x, sy + distance - abs(sx - x)))
            x += 1
print(empty)
with open("vstup.txt") as vstup:
    for line in vstup:
        #print(line)
        sline = line.rstrip().replace(",", "").replace(":", "").split(" ")
        sx = int(sline[2][2:])
        sy = int(sline[3][2:])
        bx = int(sline[8][2:])
        by = int(sline[9][2:])
        distance = abs(sx - bx) + abs(sy - by)
        removed = set()
        for x, y in empty:
            if abs(sx - x) + abs(sy - y) <= distance or not(0<=x<=4000000) or not(0<=y<=4000000):
                removed.add((x, y))
        empty.difference_update(removed)
        removed = set()
print(empty)
for p in empty:
    x, y = p
    print(x * 4000000 + y)
