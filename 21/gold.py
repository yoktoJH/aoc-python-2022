solved = {}
riddles = {}
with open("vstup.txt") as vstup:
    for line in vstup:
        sline = line.rstrip().replace(":", "").split(" ")
        if len(sline) == 2:
            solved[sline[0]] = sline[1]
        else:
            riddles[sline[0]] = sline[1:]


def solve(riddles, solved):
    solutions = solved.copy()
    stack = ["root"]
    while stack:
        if stack[-1] not in solutions:
            to_solve = riddles[stack[-1]]
            left, op, right = to_solve
            if left not in solutions or right not in solutions:
                stack.append(left)
                stack.append(right)
                continue
            solutions[stack[-1]] = str(eval(solutions[left] + op + solutions[right]))
        stack.pop()
    return solutions


x = solve(riddles, solved)
difference = eval(x["wdzt"] + "-" + x["dffc"])

solved["humn"] = str(int(solved["humn"]) + 1)
x = solve(riddles, solved)
difference2 = eval(x["wdzt"] + "-" + x["dffc"])

increase = difference / (difference - difference2)
human = 608 + int(increase) - 123090000

riddles["root"][1] = "=="

while x["root"] != "True":
    human -= 1
    solved["humn"] = str(human)
    x = solve(riddles, solved)
    if human % 100 == 0:
        print(human)
        print(eval(x["wdzt"] + "-" + x["dffc"]))
        print()
print(human)
