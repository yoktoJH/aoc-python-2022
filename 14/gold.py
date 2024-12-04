with open("vstup.txt") as vstup:
    rocks = set()
    max_y = 0
    for line in vstup:
        sline = line.rstrip().split(" -> ")
        previous_rock = sline[0]
        x, y = previous_rock.split(",")
        xp = int(x)
        yp = int(y)
        for i in range(1, len(sline)):
            next_rock = sline[i]
            xn, yn = next_rock.split(",")
            xn = int(xn)
            yn = int(yn)
            if xn != xp:
                step = -((xp - xn) // abs(xp - xn))
                for val in range(xp, xn + step, step):
                    rocks.add((val, yp))
            else:
                step = -((yp - yn) // abs(yp - yn))
                for val in range(yp, yn + step, step):
                    rocks.add((xp, val))
            if yp > max_y:
                max_y = yp
            if yn > max_y:
                max_y = yn
            previous_rock = next_rock
            xp = xn
            yp = yn
sand = set()
sandx = 500
sandy = 0
bottom = max_y + 2
while (500,0) not in sand:
    if (sandx, sandy + 1) not in sand \
            and (sandx, sandy + 1) not in rocks and sandy + 1 != bottom:
        sandy += 1
    elif (sandx - 1, sandy + 1) not in sand \
            and (sandx - 1, sandy + 1) not in rocks and sandy + 1 != bottom:
        sandy += 1
        sandx -= 1
    elif (sandx + 1, sandy + 1) not in sand \
            and (sandx + 1, sandy + 1) not in rocks and sandy + 1 != bottom:
        sandy += 1
        sandx += 1
    else:
        sand.add((sandx, sandy))
        sandx = 500
        sandy = 0
print(len(sand))
