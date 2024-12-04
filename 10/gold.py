with open("vstup.txt") as vstup:
    cycle = 0
    score = 0
    x = 1
    cycles = []
    for line in vstup:
        sline = line.rstrip()
        if sline == "noop":
            cycles.append(x)
        else:
            _, val = sline.split(" ")
            n = int(val)
            for i in range(2):
                cycles.append(x)
            x += n
    screen = []
    for i in range(6):
        screen.append(["." for _ in range(40)])
    cycle_index = 0
    for row in screen:
        for i in range(len(row)):
            if abs(cycles[cycle_index] - i) <=1:
                row[i] = "#"
            cycle_index+=1
    for row in screen:
        for pixel in row:
            print(pixel,end="")
        print()
