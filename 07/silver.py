class Adresar:
    def __init__(self, name, parent):
        self.children = []
        self.name = name
        self.parent = parent
        self.size = 0
        self.files = set()

    def add_child(self, adresar):
        self.children.append(adresar)

    def add_file(self, size, name):
        self.files.add(name)
        self.size += size


with open("vstup.txt") as vstup:
    root = Adresar("/", None)
    current_dir = root
    for line in vstup:
        sline = line.rstrip().split(" ")
        if sline == ["$", "cd", ".."] and current_dir.name != "/":
            current_dir = current_dir.parent
        elif sline[0] == "$" and sline[1] == "cd":
            for child in current_dir.children:
                if child.name == sline[2]:
                    current_dir = child
                    break
        elif sline[0] == "$" and sline[1] == "ls":
            pass
        elif sline[0] == "dir":
            current_dir.add_child(Adresar(sline[1],current_dir))
        else:
            current_dir.add_file(int(sline[0]),sline[1])


def sumoftree(root):
    size = root.size
    ciselko =0
    for x in root.children:
        csize,presucty = sumoftree(x)
        size += csize
        ciselko += presucty
    if size<100000:
        ciselko += size
    return (size,ciselko)
sumoftree(root)
print(sumoftree(root))

needtoempty = 30000000 - (70000000 - root.size)
