with open("vstup.txt") as vstup:
    score = 0
    row_max = -1
    col_max = [-1 for _ in range(101)]
    atrocity = []
    atrocity2 = []
    for i in range(99):
        atrocity2.append([])
    for line in vstup:
        sline = line.rstrip()
        atrocity.append([])
        for i, x in enumerate(sline):
            atrocity[-1].append(int(x))
            atrocity2[i].append(int(x))
    atrocsur = set()
    for i in range(1, len(atrocity) - 1):
        for j in range(1, len(atrocity[0]) - 1):
            if max(atrocity[i][:j]) < atrocity[i][j] or max(
                    atrocity[i][j + 1:]) < atrocity[i][j]:
                score += 1
                atrocsur.add((i,j))
            elif max(atrocity2[j][:i]) < atrocity2[j][i] or max(
                    atrocity2[j][i + 1:]) < atrocity2[j][i]:
                score += 1

print(score+len(atrocity)*2+(len(atrocity[0])-2)*2)

