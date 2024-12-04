suma = 0
with open("vstup.txt") as vstup:
    for y, line in enumerate(vstup):
        sline = line.rstrip()[::-1]
        num = 0
        for power in range(len(sline)):
            if sline[power] == "-":
                num += (-1) * 5 ** power
            elif sline[power] == "=":
                num += (-2) * 5 ** power
            else:
                num += int(sline[power]) * 5 ** power
        suma += num
print(suma)
patkove = ""
while suma > 0:
    zvysok = suma % 5
    if zvysok == 4:
        patkove = "-"+patkove
        suma = (suma+5)//5
    elif zvysok == 3:
        patkove = "="+patkove
        suma = (suma+5)//5
    else:
        patkove = str(zvysok) + patkove
        suma = (suma) // 5
print(patkove)