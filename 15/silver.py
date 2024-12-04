with open("vstup.txt") as vstup:
    empty = set()
    for line in vstup:
        sline = line.rstrip().replace(",", "").replace(":", "").split(" ")
        sx = int(sline[2][2:])
        sy = int(sline[3][2:])
        bx = int(sline[8][2:])
        by = int(sline[9][2:])
        distance = abs(sx - bx) + abs(sy - by)
        y = 2000000
        yd = abs(sy - y)
        x = sx - distance + yd - 1
        while x < sx + distance - yd + 1:
            emtpty_dist = abs(sx - x) + yd
            if emtpty_dist <= distance and not (bx == x and by == y):
                empty.add(x)
            x += 1
print(len(empty))
