from collections import deque
from tqdm import tqdm
with open("vstup.txt") as vstup:
    tunnels = {}
    flow_rate = {}
    nonzero_valves = {"AA"}
    for line in vstup:
        flow, tunnel = line.rstrip().split(";")
        sflow = flow.split(" ")
        rate = sflow[-1].split("=")
        if int(rate[-1]) != 0:
            nonzero_valves.add(sflow[1])
        flow_rate[sflow[1]] = int(rate[-1])
        stunnels = tunnel.replace(",", "").split(" ")
        leads_to = [word for word in stunnels if
                    word not in {"", "tunnels", "tunnel", "lead", "to", "valve", "valves", "leads"}]
        tunnels[sflow[1]] = leads_to


def bfs(start):
    previous = {}
    distances = {start: 0}
    queue = deque([start])
    while queue:
        vent = queue.popleft()
        if distances.get(vent) is None:
            distances[vent] = distances[previous[vent]] + 1
        for x in tunnels[vent]:
            if previous.get(x) is None:
                previous[x] = vent
                queue.append(x)
    return distances


bfs_trees = {}
for valve in nonzero_valves:
    bfs_trees[valve] = bfs(valve)

# for x in bfs_trees.items():
#     print(x)

solutions = []


def recursive_solving(current_valve, not_opened, pressure, minutes, order_of_select):
    if minutes == 0 or not not_opened:
        solutions.append(order_of_select.copy())
        return pressure
    out = []
    distances = bfs_trees[current_valve]
    for valve in not_opened:
        distance = distances[valve]
        new_minutes = minutes - distance - 1
        if new_minutes >= 0:
            new_pressure = flow_rate[valve] * new_minutes
            order_of_select[valve] = new_minutes
            out.append(
                recursive_solving(valve, not_opened - {valve}, pressure + new_pressure, new_minutes, order_of_select))
            order_of_select.pop(valve)
    if out:
        return max(out)
    return 0


recursive_solving("AA", nonzero_valves - {"AA"}, 0, 26, {})

max_pressure = 0
for human in tqdm(solutions):
    human_order_vzor = sorted(human.items(), key=lambda x: x[1])
    for elephant in solutions:
        visited = set()
        pressure = 0
        human_order = human_order_vzor.copy()
        elephant_order = sorted(elephant.items(), key=lambda x: x[1])
        while elephant_order and human_order:
            if human_order[-1][1] > elephant_order[-1][1]:
                if human_order[-1][0] not in visited:
                    pressure += flow_rate[human_order[-1][0]]*human_order[-1][1]
                    visited.add(human_order[-1][0])
                human_order.pop()

            else:
                if elephant_order[-1][0] not in visited:
                    pressure += flow_rate[elephant_order[-1][0]] * elephant_order[-1][1]
                    visited.add(elephant_order[-1][0])
                elephant_order.pop()
        if pressure > max_pressure:
            max_pressure = pressure

print(max_pressure)