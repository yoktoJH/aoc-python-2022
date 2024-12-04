with open("vstup.txt") as vstup:
    superstring = vstup.readline()
    for i in range(len(superstring)):
        block = superstring[i:i+4]
        if len(set(block))==4:
            print(i+4)
            break