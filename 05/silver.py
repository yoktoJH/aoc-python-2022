with open("vstup.txt") as vstup:
    stacks = [[] for _ in range(9)]
    for _ in range(8):
        line = vstup.readline()
        sline = line.replace("\n","").split()
        for i,x in enumerate(sline):
            if x[1].isalpha():
                stacks[i].insert(0,x[1])
    print(stacks)
    for line in vstup:
        sline = line.rstrip().split()
        for i in range(int(sline[1])):
            if stacks[int(sline[3])-1]:
                stacks[int(sline[5])-1].append(stacks[int(sline[3])-1].pop())
    for stack in stacks:
        print(stack[-1])




