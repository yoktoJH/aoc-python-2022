with open("vstup.txt") as vstup:


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
    max_scenic = 0
    for i in range(1, len(atrocity) - 1):
        for j in range(1, len(atrocity[0]) - 1):
            x = atrocity[i][j]
            if max(atrocity[i][:j]) < x:
                final = 1
                score = 0
                for k in range(j+1,len(atrocity[0])):
                    score += 1
                    if atrocity[i][k]>=x:
                        break
                final*=score
                score = 0
                for k in range(i+1,len(atrocity2[0])):
                    score+=1
                    if atrocity2[j][k]>=x:
                        break
                final *= score
                score = 0
                for k in range(i-1,-1,-1):
                    score+=1
                    if atrocity2[j][k]>=x:
                        break
                final *= score
                score = 0
                for k in range(j - 1, -1, -1):
                    score += 1
                    if atrocity[i][k] >= x:
                        break
                final *= score
                if final>max_scenic:
                    max_scenic = final

            elif max(atrocity[i][j + 1:]) < atrocity[i][j]:
                final = 1
                score = 0
                for k in range(j + 1, len(atrocity[0])):
                    score += 1
                    if atrocity[i][k] >= x:
                        break
                final *= score
                score = 0
                for k in range(i + 1, len(atrocity2[0])):
                    score += 1
                    if atrocity2[j][k] >= x:
                        break
                final *= score
                score = 0
                for k in range(i - 1, -1, -1):
                    score += 1
                    if atrocity2[j][k] >= x:
                        break
                final *= score
                score = 0
                for k in range(j - 1, -1, -1):
                    score += 1
                    if atrocity[i][k] >= x:
                        break
                final *= score
                if final > max_scenic:
                    max_scenic = final

            elif max(atrocity2[j][:i]) < atrocity2[j][i]:
                final = 1
                score = 0
                for k in range(j + 1, len(atrocity[0])):
                    score += 1
                    if atrocity[i][k] >= x:
                        break
                final *= score
                score = 0
                for k in range(i + 1, len(atrocity2[0])):
                    score += 1
                    if atrocity2[j][k] >= x:
                        break
                final *= score
                score = 0
                for k in range(i - 1, -1, -1):
                    score += 1
                    if atrocity2[j][k] >= x:
                        break
                final *= score
                score = 0
                for k in range(j - 1, -1, -1):
                    score += 1
                    if atrocity[i][k] >= x:
                        break
                final *= score
                if final > max_scenic:
                    max_scenic = final

            elif max(atrocity2[j][i + 1:]) < atrocity2[j][i]:
                final = 1
                score = 0
                for k in range(j + 1, len(atrocity[0])):
                    score += 1
                    if atrocity[i][k] >= x:
                        break
                final *= score
                score = 0
                for k in range(i + 1, len(atrocity2[0])):
                    score += 1
                    if atrocity2[j][k] >= x:
                        break
                final *= score
                score = 0
                for k in range(i - 1, -1, -1):
                    score += 1
                    if atrocity2[j][k] >= x:
                        break
                final *= score
                score = 0
                for k in range(j - 1, -1, -1):
                    score += 1
                    if atrocity[i][k] >= x:
                        break
                final *= score
                if final > max_scenic:
                    max_scenic = final

print(max_scenic)
