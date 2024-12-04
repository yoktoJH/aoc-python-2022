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

solved["humn"] = str(3952673930912)
x = solve(riddles, solved)
print(x["root"],x["wdzt"],x["dffc"])

