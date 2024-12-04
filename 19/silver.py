def dig_geode(minute, materials, robots):
    if minute == 24:
        return materials["geode"]
    out = [materials["geode"]]
    new_materials = {}
    for key in materials:
        new_materials[key] = materials[key] + robots[key]
    # do nothing
    out.append(dig_geode(minute + 1, new_materials.copy(), robots.copy()))
    if materials["ore"] >= ore_cost:
        new_materials["ore"] -= ore_cost
        robots["ore"] += 1
        out.append(dig_geode(minute + 1, new_materials.copy(), robots.copy()))
        robots["ore"] -= 1
        new_materials["ore"] += ore_cost

    if materials["ore"] >= clay_cost:
        new_materials["ore"] -= clay_cost
        robots["clay"] += 1
        out.append(dig_geode(minute + 1, new_materials.copy(), robots.copy()))
        robots["clay"] -= 1
        new_materials["ore"] += clay_cost

    if materials["ore"] >= obsidian_cost[0] and materials["clay"] >= obsidian_cost[1]:
        new_materials["ore"] -= obsidian_cost[0]
        new_materials["clay"] -= obsidian_cost[1]
        robots["obsidian"] += 1
        out.append(dig_geode(minute + 1, new_materials.copy(), robots.copy()))
        robots["obsidian"] -= 1
        new_materials["ore"] += obsidian_cost[0]
        new_materials["clay"] += obsidian_cost[1]

    if materials["ore"] >= geode_cost[0] and materials["obsidian"] >= geode_cost[1]:
        new_materials["ore"] -= geode_cost[0]
        new_materials["obsidian"] -= geode_cost[1]
        robots["geode"] += 1
        out.append(dig_geode(minute + 1, new_materials.copy(), robots.copy()))
        robots["geode"] -= 1
        new_materials["ore"] += geode_cost[0]
        new_materials["obsidian"] += geode_cost[1]
    return max(out)


with open("vstup.txt") as vstup:
    score = 0
    for line in vstup:
        sline = line.rstrip().replace("Blueprint ", "").replace(": Each ore robot costs", "").replace(
            " ore. Each clay robot costs", "").replace(" ore. Each obsidian robot costs", "").replace(" ore and", ""
                                                                                                      ).replace(
            " clay. Each geode robot costs", "").replace(" obsidian.", "").split(" ")
        bluelprint_id = int(sline[0])
        ore_cost = int(sline[1])
        clay_cost = int(sline[2])
        obsidian_cost = (int(sline[3]), int(sline[4]))
        geode_cost = (int(sline[5]), int(sline[6]))
        mat = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
        rob = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
        x = dig_geode(1, mat, rob)
        score += bluelprint_id * x
print(score)
