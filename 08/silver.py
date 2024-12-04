head = [0, 0]
tail = [0, 0]
visited = set()
visited.add((tail[0], tail[1]))
with open("vstup.txt") as vstup:
    for line in vstup:
        sline = line.rstrip().split(" ")
        if sline[0] == "U":
            difference = (0, 1)
        elif sline[0] == "D":
            difference = (0, -1)
        elif sline[0] == "L":
            difference = (-1, 0)
        elif sline[0] == "R":
            difference = (1, 0)

        # pohyb
        xdiff, ydiff = difference
        for i in range(int(sline[1])):
            head[0] += xdiff
            head[1] += ydiff
            if head[0] == tail[0]:
                if head[1] - tail[1] > 1:
                    tail[1] += 1
                    visited.add((tail[0], tail[1]))
                elif head[1] - tail[1] < -1:
                    tail[1] += -1
                    visited.add((tail[0], tail[1]))

            elif head[1] == tail[1]:
                if head[0] - tail[0] > 1:
                    tail[0] += 1
                    visited.add((tail[0], tail[1]))
                elif head[0] - tail[0] < -1:
                    tail[0] += -1
                    visited.add((tail[0], tail[1]))
            else:
                if head[0] - tail[0] > 1:
                    tail[0] += 1
                    tail[1] += head[1] - tail[1]
                    visited.add((tail[0], tail[1]))
                elif head[0] - tail[0] < -1:
                    tail[0] += -1
                    tail[1] += head[1] - tail[1]
                    visited.add((tail[0], tail[1]))
                elif head[1] - tail[1] > 1:
                    tail[1] += 1
                    tail[0] += head[0] - tail[0]
                    visited.add((tail[0], tail[1]))
                elif head[1] - tail[1] < -1:
                    tail[1] += -1
                    tail[0] += head[0] - tail[0]
                    visited.add((tail[0], tail[1]))
print(len(visited))
                