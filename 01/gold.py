with open("vstup.txt") as vstup:
    elves = []
    elf = 0
    for line in vstup:
        if line == "\n":
            elves.append(elf)
            elf = 0
        else:
            elf += int(line.replace("\n", ""))

    out = 0
    for i in range(3):
        out+=max( elves)
        elves.pop(elves.index(max(elves)))
    print(out)