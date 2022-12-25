def print_set(elves):
    for j in range(80):
        line = ""
        for i in range(80):
            line += "#" if (i, j) in elves else "."
        print(line)


elves = set()
with open("input2.txt", "r") as f:
    count = 0
    for line in f:
        line = line[:-1]
        for i in range(len(line)):
            if line[i]=="#":
                elves.add((i, count))
        count += 1

# print_set(elves)

# current_priority = 0
# [N,S,W,E]
dirs = (
    ((0,-1), (-1,-1), (1,-1)),
    ((0,1),(-1,1),(1,1)),
    ((-1,0),(-1,-1),(-1,1)),
    ((1,0),(1,-1),(1,1))
)
scan = (
    (0,1),(0,-1),(1,0),(-1,0),
    (1,1),(1,-1),(-1,-1),(-1,1),
)
# current_priority = (current_priority+1)%4

for x in range(10):
    proposed2orig = {}
    dupes = set()
    for elf in elves:
        not_alone = False
        for dir in scan:
            checker = (elf[0]+dir[0],elf[1]+dir[1])
            not_alone = not_alone or (checker in elves)
        if not not_alone:
            continue

        for dir in range(4):
            occupied = False
            for loc in dirs[(x+dir)%4]:
                occupied = occupied or ((elf[0]+loc[0],elf[1]+loc[1]) in elves)
            if not occupied:
                prop = (elf[0]+dirs[(x+dir)%4][0][0],elf[1]+dirs[(x+dir)%4][0][1])
                if prop in proposed2orig:
                    dupes.add(prop)
                proposed2orig[(elf[0]+dirs[(x+dir)%4][0][0],elf[1]+dirs[(x+dir)%4][0][1])] = elf
                break
            

    for dupe in dupes:
        if dupe in proposed2orig:
            del proposed2orig[dupe]

    for i in proposed2orig:
        elves.remove(proposed2orig[i])
    for i in proposed2orig:
        elves.add(i)

# print_set(elves)
# width = [3,3]
# height = [3,3]
# for elf in elves:
#     width[0] = min(width[0], elf[0])
#     width[1] = max(width[1], elf[0])
#     height[0] = min(height[0], elf[1])
#     height[1] = max(height[1], elf[1])

# print(width, height)
# rect = ((width[1]-width[0])+1)*((height[1]-height[0])+1)
# print(rect - len(elves))


# 3795 too low

# print(len(elves))
# print(len(proposed2orig), len(dupes))

# two stages