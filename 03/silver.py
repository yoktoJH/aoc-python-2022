with open("vstup.txt") as vstup:
    score = 0
    for line in vstup:
        line1 = line[0:len(line) // 2]
        line2 = line[len(line) // 2:]
        for x in line1:
            if x in line2:
                if x.isupper():
                    score += ord(x) - 38
                else:
                    score += ord(x) - 96
                break
    print(score)
