with open("vstup.txt") as vstup:
    score = 0
    for line in vstup:
        sline = line.rstrip().split(",")
        elf1 = sline[0].split("-")
        elf2 = sline[1].split("-")
        if int(elf2[0]) <= int(elf1[0]) <= int(elf2[1]) or int(elf2[0]) <= int(
                elf1[1]) <= int(elf2[1]):
            score += 1
        elif int(elf1[0]) <= int(elf2[0]) <= int(elf1[1]) or int(
                elf1[0]) <= int(elf2[1]) <= int(elf1[1]):
            score += 1
    print(score)
