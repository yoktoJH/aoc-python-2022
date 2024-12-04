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


def get_instruction(instructions):
    if instructions[0] == "L":
        return "L", 1
    if instructions[0] == "R":
        return "R", 1
    j = 0
    while j < len(instructions) and instructions[j] != "R" and instructions[j] != "L":
        j += 1
    return instructions[0:j], j


def get_position(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == ".":
                return x, y


def opposite_side(pos, previous_dir):
    x, y = pos
    dirx, diry = -previous_dir[0], -previous_dir[1]
    while (0 <= x + dirx < max_len and 0 <= y + diry < len(board)) and board[y + diry][x + dirx] != " ":
        x += dirx
        y += diry
    return x, y


x, y = get_position(board)
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
            x += direction[0]
            y += direction[1]
            if not (0 <= x < max_len and 0 <= y < len(board)) or board[y][x] == " ":
                opposite_x, opposite_y = opposite_side((x, y), direction)
                if board[opposite_y][opposite_x] == "#":
                    x -= direction[0]
                    y -= direction[1]
                    break
                else:
                    x = opposite_x
                    y = opposite_y
            elif board[y][x] == "#":
                x -= direction[0]
                y -= direction[1]
                break
direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
print((y+1) * 1000 + 4 * (x+1) + direct.index(direction))

