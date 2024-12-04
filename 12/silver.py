with open("vstup.txt") as vstup:
    letters = []
    dist = []
    queue = set()
    for i, line in enumerate(vstup):
        letters.append([])
        for j, char in enumerate(line.rstrip()):
            dist.append(9999999)
            queue.add((i, j))
            if char == "S":
                start = (i, j)
                letters[-1].append("a")
                continue
            if char == "E":
                end = (i, j)
                letters[-1].append("z")
                continue
            letters[-1].append(char)


width = len(letters[0])
height = len(letters)
x, y = start
dist[x * width + y] = 0
graph = []
for i, row in enumerate(letters):
    graph.append([])
    for j, char in enumerate(row):
        edges = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x = i + dx
            y = j + dy
            if 0 <= x < height and 0 <= y < width and ord(letters[i][j]) - ord(
                    letters[x][y]) >= -1:
                edges.append((x, y))
        graph[-1].append(edges)


def min_vrchol(queue, distances):
    minimum = 9999999
    out = None
    for x, y in queue:
        if distances[x * width + y] < minimum:
            minimum = distances[x * width + y]
            out = (x, y)

    return out

predosly = 0
ex,ey = end
zmenene = {start}
while dist[ex*width+ ey] != 999999:
    vrchol = min_vrchol(zmenene, dist)
    if vrchol is None:
        break
    else:
        queue.remove(vrchol)
        zmenene.remove(vrchol)
        x,y = vrchol
    predosly = dist[x * width + y ]
    for x1,y1 in graph[x][y]:
        if (x1,y1) in queue:
            zmenene.add((x1,y1))
        dist[x1 * width + y1 ] = predosly+1
x1,y1 =end
print(dist[x1 * width + y1 ])
print(start)