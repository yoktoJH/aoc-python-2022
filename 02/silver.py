with open("vstup.txt") as vstup:
    score = 0
    for line in vstup:
        enemy, me = line.rstrip().split(" ")
        if me == "X":  # rock
            rock = {"A": 4, "B": 1, "C": 7}
            score+= rock[enemy]
        if me == "Y":  # paper
            paper = {"A": 8, "B": 5, "C": 2}
            score += paper[enemy]
        if me == "Z":  # scissors
            scissors = {"A": 3, "B": 9, "C": 6}
            score += scissors[enemy]
    print(score)