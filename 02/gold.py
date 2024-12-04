with open("vstup.txt") as vstup:
    score = 0
    for line in vstup:
        enemy, me = line.rstrip().split(" ")
        if me == "X":  # lose
            outcomes = {"A": 3, "B": 1, "C": 2}
            score += outcomes[enemy]
        if me == "Y":  # tie
            outcomes= {"A": 4, "B": 5, "C": 6}
            score += outcomes[enemy]
        if me == "Z":  # win
            outcomes = {"A": 8, "B": 9, "C": 7}
            score += outcomes[enemy]
    print(score)