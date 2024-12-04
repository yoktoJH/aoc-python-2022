with open("vstup.txt") as vstup:
    score = 0
    for line in vstup:
        line1 = vstup.readline().rstrip()
        line2 = vstup.readline().rstrip()
        for x in line:
            if x in line2 and x in line1:
                if x.isupper():
                    score += ord(x) - 38
                else:
                    score += ord(x) - 96
                break
    print(score)
