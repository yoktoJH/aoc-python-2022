from collections import deque

with open("vstup.txt") as vstup:
    letters = []
    dist_orig = []
    queue_orig = set()
    for i, line in enumerate(vstup):
        letters.append([])
        for j, char in enumerate(line.rstrip()):
            dist_orig.append(9999999)
            queue_orig.add((i, j))
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
graph = []
starts = []
for i, row in enumerate(letters):
    graph.append([])
    for j, char in enumerate(row):
        edges = []
        if char == "a":
            starts.append((i, j))
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


ends = []
for start in starts:
    queue = queue_orig.copy()
    dist = dist_orig.copy()
    dist[start[0] * width + start[1]] = 0
    predosly = 0
    ex, ey = end
    zmenene = deque([start])
    while zmenene:
        vrchol = zmenene.popleft()
        x, y = vrchol
        predosly = dist[x * width + y]
        for x1, y1 in graph[x][y]:
            if (x1, y1) in queue:
                queue.remove((x1, y1))
                zmenene.append((x1,y1))
            dist[x1 * width + y1] = predosly + 1
    x1, y1 = end
    ends.append(dist[x1 * width + y1])
print(min(ends))
