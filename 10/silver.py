with open("vstup.txt") as vstup:
    interested = [20,60,100,140,180,220]
    cycle = 0
    score = 0
    x = 1
    for line in vstup:
        if not interested:
            break
        sline = line.rstrip()
        if sline == "noop":
            cycle+=1
            if cycle == interested[0]:
                score += x*interested[0]
                interested.pop(0)
        else:
            _,val = sline.split(" ")
            n = int(val)
            for i in range(2):
                cycle += 1
                if interested and cycle == interested[0]:
                    score += x * interested[0]
                    interested.pop(0)
            x += n
print(score)