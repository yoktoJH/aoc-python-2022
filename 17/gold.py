from tqdm import tqdm
with open("vstup.txt") as vstup:
    for line in vstup:
        air_currents = line.rstrip()
chamber = [0 for i in range(7)]
line = [(0, 0), (1, 0), (2, 0), (3, 0)]
plus = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
an_l = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
stlp = [(0, 0), (0, 1), (0, 2), (0, 3)]
square = [(0, 0), (0, 1), (1, 0), (1, 1)]
shapes = [line, plus, an_l, stlp, square]

