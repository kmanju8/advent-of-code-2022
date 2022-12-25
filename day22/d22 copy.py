# worked for part 1
grid = {}
with open("map.txt", "r") as f:
    count = 0
    for line in f:
        line = line[:-1]
        for i in range(len(line)):
            if line[i]!=" ":
                grid[(i, count)] = line[i]
        count += 1

dir = {
    0: [1,0],
    1: [0,1],
    2: [-1,0],
    3: [0,-1]
}

# for legit
current = (50,0)
# for test
# current = (8,0)
facing = 0
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line == "L":
            facing = (facing-1)%4
        elif line == "R":
            facing = (facing+1)%4
        else:
            for i in range(int(line)):
                next_loc = tuple([current[i]+dir[facing][i] for i in range(2)])
                if next_loc in grid:
                    if grid[next_loc] == "#":
                        break
                    else:
                        current = next_loc
                else:
                    # wrapping logic
                    next_loc = tuple([next_loc[i]-dir[facing][i] for i in range(2)])
                    while next_loc in grid:
                        next_loc = tuple([next_loc[i]-dir[facing][i] for i in range(2)])
                    next_loc = tuple([next_loc[i]+dir[facing][i] for i in range(2)])
                    if next_loc in grid:
                        if grid[next_loc] == "#":
                            break
                        else:
                            current = next_loc

print(4*(current[0]+1)+1000*(current[1]+1)+ facing)
print(current[1]+1,current[0]+1, facing)
# 132203 too high
#  31568 correct