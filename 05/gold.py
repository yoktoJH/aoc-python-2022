with open("vstup.txt") as vstup:
    stacks = [[] for _ in range(9)]
    for _ in range(8):
        line = vstup.readline()
        sline = line.rstrip().split()
        for i,x in enumerate(sline):
            if x[1].isalpha():
                stacks[i].insert(0,x[1])
    print(stacks)
    for line in vstup:
        sline = line.rstrip().split()
        stacks[int(sline[5])-1] += stacks[int(sline[3])-1][-(int(sline[1])):]
        stacks[int(sline[3]) - 1] = stacks[int(sline[3]) - 1][0:-(int(sline[1]))]
    for stack in stacks:
        print(stack[-1])