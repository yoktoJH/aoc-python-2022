with open("vstup.txt") as vstup:
    superstring = vstup.readline()
    for i in range(len(superstring)):
        block = superstring[i:i + 14]
        if len(set(block)) == 14:
            print(i + 14)
            break