class Directory:
    def __init__(self, name, parent):
        self.name = name
        # contents can have directories or file sizes
        self.contents = []
        self.parent = parent

    def size(self, aocvar):
        total = 0
        for file in self.contents:
            if isinstance(file, Directory):
                total += file.size(aocvar)
            else:
                total += file
        
        if total < 100000:
            aocvar.append(total)
        return total


current_directory = Directory("/", None)
root = current_directory

with open('input.txt', 'r') as f:
    for line in f:
        line = line.split()
        if line[0] == "$" and line[1] == "cd":
            if line[2] == "..":
                current_directory = current_directory.parent
            else:
                for directory in current_directory.contents:
                    if isinstance(directory, Directory) and directory.name == line[2]:
                        current_directory = directory
                        break
        else:
            if line[0] == "dir":
                current_directory.contents.append(Directory(line[1], current_directory))
            else:
                current_directory.contents.append(int(line[0]))

aocvar = []
root.size(aocvar)
print(sum(aocvar))
