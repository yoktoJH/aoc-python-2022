tails = [[0, 0] for _ in range(10)]
visited = set()
visited.add((0, 0))
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
        for _ in range(int(sline[1])):
            tails[0][0] += xdiff
            tails[0][1] += ydiff
            for i in range(9):
                head = tails[i]
                tail = tails[i + 1]
                if head[0] == tail[0]:
                    if head[1] - tail[1] > 1:
                        tail[1] += 1
                    elif head[1] - tail[1] < -1:
                        tail[1] += -1
                elif head[1] == tail[1]:
                    if head[0] - tail[0] > 1:
                        tail[0] += 1

                    elif head[0] - tail[0] < -1:
                        tail[0] += -1
                else:
                    if head[0] - tail[0] > 1:
                        tail[0] += 1
                        if head[1] - tail[1]>0:
                            tail[1] += 1
                        else:
                            tail[1] += -1
                    elif head[0] - tail[0] < -1:
                        tail[0] += -1
                        if head[1] - tail[1] > 0:
                            tail[1] += 1
                        else:
                            tail[1] += -1

                    elif head[1] - tail[1] > 1:
                        tail[1] += 1
                        if head[0] - tail[0] > 0:
                            tail[0] += 1
                        else:
                            tail[0] += -1

                    elif head[1] - tail[1] < -1:
                        tail[1] += -1
                        if head[0] - tail[0] > 0:
                            tail[0] += 1
                        else:
                            tail[0] += -1
                if i+1 == 9:
                    visited.add((tails[9][0], tails[9][1]))
print(len(visited))
