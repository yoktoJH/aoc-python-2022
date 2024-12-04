board = []
max_len = 0
with open("vstup.txt") as vstup:
    for line in vstup:
        line = line.rstrip()
        sline = []
        if len(line) > max_len:
            max_len = len(line)
        for char in line:
            sline.append(char)
        board.append(sline)

for row in board:
    if len(row) < max_len:
        for _ in range(max_len - len(row)):
            row.append(" ")
instructions = "".join(board.pop())
board.pop()

B = []
for i in range(50):
    line = []
    for j in range(50, 100):
        line.append(board[i][j])
    B.append(line)
A = []
for i in range(50):
    line = []
    for j in range(100, 150):
        line.append(board[i][j])
    A.append(line)
C = []
for i in range(50, 100):
    line = []
    for j in range(50, 100):
        line.append(board[i][j])
    C.append(line)
D = []
for i in range(100, 150):
    line = []
    for j in range(50, 100):
        line.append(board[i][j])
    D.append(line)
E = []
for i in range(100, 150):
    line = []
    for j in range(50):
        line.append(board[i][j])
    E.append(line)
F = []
for i in range(150, 200):
    line = []
    for j in range(50):
        line.append(board[i][j])
    F.append(line)
for line in B:
    print("".join(line))

sides = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F}


def get_instruction(instructions):
    if instructions[0] == "L":
        return "L", 1
    if instructions[0] == "R":
        return "R", 1
    j = 0
    while j < len(instructions) and instructions[j] != "R" and instructions[j] != "L":
        j += 1
    return instructions[0:j], j


def edge_case(side, x, y, direction):
    if side == "A":
        if direction == (-1, 0):
            x = 49
            if B[y][x] == "#":
                return True, "B", x, y, direction
            else:
                return False, "B", x, y, direction
        if direction == (1, 0):
            x = 49
            y = 49 - y
            if D[y][x] == "#":
                return True, "D", x, y, direction
            else:
                return False, "D", x, y, (-1, 0)
        if direction == (0, 1):
            y = x
            x = 49
            if C[y][x] == "#":
                return True, "C", x, y, direction
            else:
                return False, "C", x, y, (-1, 0)
        if direction == (0, -1):
            y = 49
            if F[y][x] == "#":
                return True, "F", x, y, direction
            else:
                return False, "F", x, y, (0, -1)
    elif side == "B":
        if direction == (-1, 0):
            x = 0
            y = 49 - y
            if E[y][x] == "#":
                return True, "E", x, y, direction
            else:
                return False, "E", x, y, (1, 0)
        if direction == (1, 0):
            x = 0
            if A[y][x] == "#":
                return True, "A", x, y, direction
            else:
                return False, "A", x, y, direction
        if direction == (0, 1):
            y = 0
            if C[y][x] == "#":
                return True, "C", x, y, direction
            else:
                return False, "C", x, y, direction
        if direction == (0, -1):
            y = x
            x = 0
            if F[y][x] == "#":
                return True, "F", x, y, direction
            else:
                return False, "F", x, y, (1, 0)
    elif side == "C":
        if direction == (-1, 0):
            x = y
            y = 0
            if E[y][x] == "#":
                return True, "E", x, y, direction
            else:
                return False, "E", x, y, (0, 1)
        if direction == (1, 0):
            x = y
            y = 49
            if A[y][x] == "#":
                return True, "A", x, y, direction
            else:
                return False, "A", x, y, (0, -1)
        if direction == (0, 1):
            y = 0
            if D[y][x] == "#":
                return True, "D", x, y, direction
            else:
                return False, "D", x, y, direction
        if direction == (0, -1):
            y = 49
            if B[y][x] == "#":
                return True, "B", x, y, direction
            else:
                return False, "B", x, y, direction
    elif side == "D":
        if direction == (-1, 0):
            x = 49
            if E[y][x] == "#":
                return True, "E", x, y, direction
            else:
                return False, "E", x, y, direction
        if direction == (1, 0):
            y = 49 - y
            x = 49
            if A[y][x] == "#":
                return True, "A", x, y, direction
            else:
                return False, "A", x, y, (-1, 0)
        if direction == (0, 1):
            y = x
            x = 49
            if F[y][x] == "#":
                return True, "F", x, y, direction
            else:
                return False, "F", x, y, (-1, 0)
        if direction == (0, -1):
            y = 49
            if C[y][x] == "#":
                return True, "C", x, y, direction
            else:
                return False, "C", x, y, direction
    elif side == "E":
        if direction == (-1, 0):
            x = 0
            y = 49 - y
            if B[y][x] == "#":
                return True, "B", x, y, direction
            else:
                return False, "B", x, y, (1, 0)
        if direction == (1, 0):
            x = 0
            if D[y][x] == "#":
                return True, "D", x, y, direction
            else:
                return False, "D", x, y, direction
        if direction == (0, 1):
            y = 0
            if F[y][x] == "#":
                return True, "F", x, y, direction
            else:
                return False, "F", x, y, direction
        if direction == (0, -1):
            y = x
            x = 0
            if C[y][x] == "#":
                return True, "C", x, y, direction
            else:
                return False, "C", x, y, (1, 0)
    elif side == "F":
        if direction == (-1, 0):
            x = y
            y = 0
            if B[y][x] == "#":
                return True, "B", x, y, direction
            else:
                return False, "B", x, y, (0, 1)
        if direction == (1, 0):
            x = y
            y = 49
            if D[y][x] == "#":
                return True, "D", x, y, direction
            else:
                return False, "D", x, y, (0, -1)
        if direction == (0, 1):
            y = 0
            if A[y][x] == "#":
                return True, "A", x, y, direction
            else:
                return False, "A", x, y, direction
        if direction == (0, -1):
            y = 49
            if E[y][x] == "#":
                return True, "E", x, y, direction
            else:
                return False, "E", x, y, direction


x, y = 0, 0
side = "B"
direction = (1, 0)
while instructions:
    instruction, j = get_instruction(instructions)
    instructions = instructions[j:]

    if instruction == "L":
        xshift, yshift = direction
        direction = yshift, -xshift

    elif instruction == "R":
        xshift, yshift = direction
        direction = -yshift, xshift

    else:
        for p in range(int(instruction)):
            if not (0 <= x + direction[0] < 50 and 0 <= y + direction[1] < 50):
                rock, s, x1, y1, direct = edge_case(side, x + direction[0], y + direction[1], direction)
                if not rock:
                    x = x1
                    y = y1
                    direction = direct
                    side = s
            elif sides[side][y + direction[1]][x + direction[0]] != "#":
                x += direction[0]
                y += direction[1]
print(side, x, y, direction)
# x and y are relative to the side so beware of 0 indexing a that kind of stuff when calculating the final number
