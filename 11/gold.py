with open("vstup.txt") as vstup:
    monkeys = []
    for line in vstup:
        sline = line.strip().split(" ")
        if sline[0] == "Monkey":
            monkeys.append({})
            sline = vstup.readline().strip().split(" ")
            monkeys[-1]["items"] = []
            for i in range(sline.index("items:") + 1, len(sline)):
                monkeys[-1]["items"].append(int(sline[i].replace(",", "")))
            sline = vstup.readline().strip().split("= ")
            monkeys[-1]["operation"] = sline[-1]

            sline = vstup.readline().strip().split(" ")
            monkeys[-1]["div"] = int(sline[-1])

            sline = vstup.readline().strip().split(" ")
            monkeys[-1][True] = int(sline[-1])

            sline = vstup.readline().strip().split(" ")
            monkeys[-1][False] = int(sline[-1])

    for monkey in monkeys:
        print(monkey)


def operation(item, equation: str):
    out = {}
    equation2 = equation.split(" ")
    for key, x in item.items():
        if equation2[-1] == "old":
            y = x
        else:
            y = int(equation2[-1])
        if equation2[1] == "+":
            out[key] = (x + y) % key
        else:
            out[key] = (x * y) % key
    return out


for monkey in monkeys:
    items = []
    keys = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for item in monkey["items"]:
        itemd = {}
        for key in keys:
            itemd[key] = item % key
        items.append(itemd)
    monkey["items"] = items
# logic
score = [0 for i in range(len(monkeys))]
for _ in range(10000):
    for i, monkey in enumerate(monkeys):
        for ii in range(len(monkey["items"])):
            item = monkey["items"].pop(0)
            item = operation(item, monkey["operation"])
            next_monkey = monkey[item[monkey["div"]] == 0]
            monkeys[next_monkey]["items"].append(item)
            score[i] += 1

print(score)
x1 = max(score)
score.remove(x1)
x2 = max(score)
print(x1 * x2)
