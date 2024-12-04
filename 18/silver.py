with open("vstup.txt") as vstup:
    sides = 0
    bricks = set()
    for line in vstup:
        x,y,z = line.rstrip().split(",")
        x= int(x)
        y = int(y)
        z = int(z)
        sides+=6
        for sx,sy,sz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            if (x+sx,y+sy,z+sz) in bricks:
                sides-=2
        bricks.add((x,y,z))
print(sides)