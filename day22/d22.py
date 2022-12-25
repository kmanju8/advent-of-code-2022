sides = {}

# 1
for i in range(50):
    key = (50, 150+i, 0)
    val = (50+i, 150, 3)
    sides[key] = val
    sides[(val[0], val[1], (val[2]+2)%4)] = (key[0], key[1], (key[2]+2)%4)

# 2
for i in range(50):
    key = (i,99,3)
    val = (49,50+i, 0)
    sides[key] = val
    sides[(val[0], val[1], (val[2]+2)%4)] = (key[0], key[1], (key[2]+2)%4)

# 3
for i in range(50):
    key = (50+i,-1, 3)
    val = (-1,150+i, 0)
    sides[key] = val
    sides[(val[0], val[1], (val[2]+2)%4)] = (key[0], key[1], (key[2]+2)%4)

# 4
for i in range(50):
    key = (49,i, 2)
    val = (-1,149-i, 0)
    sides[key] = val
    sides[(val[0], val[1], (val[2]+2)%4)] = (key[0], key[1], (key[2]+2)%4)

# 5
for i in range(50):
    key = (i,200, 1)
    val = (100+i,-1, 1)
    sides[key] = val
    sides[(val[0], val[1], (val[2]+2)%4)] = (key[0], key[1], (key[2]+2)%4)

# 6
for i in range(50):
    key = (100,100+i, 0)
    val = (150,49-i, 2)
    sides[key] = val
    sides[(val[0], val[1], (val[2]+2)%4)] = (key[0], key[1], (key[2]+2)%4)

# 7
for i in range(50):
    key = (100,50+i,0)
    val = (100+i,50,3)
    sides[key] = val
    sides[(val[0], val[1], (val[2]+2)%4)] = (key[0], key[1], (key[2]+2)%4)



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

                    # WRAPPING

                    other_side = sides[(next_loc[0],next_loc[1],facing)]
                    next_loc, next_facing = (other_side[0],other_side[1]), other_side[2]

                    next_loc = tuple([next_loc[i]+dir[next_facing][i] for i in range(2)])
                    if grid[next_loc] == "#":
                        continue
                    else:
                        current = next_loc
                        facing = next_facing
                    # while next_loc in grid:
                    #     next_loc = tuple([next_loc[i]-dir[facing][i] for i in range(2)])
                    # next_loc = tuple([next_loc[i]+dir[facing][i] for i in range(2)])
                    # if next_loc in grid:
                    #     if grid[next_loc] == "#":
                    #         break
                    #     else:
                    #         current = next_loc

print(4*(current[0]+1)+1000*(current[1]+1)+ facing)
print(current[1]+1,current[0]+1, facing)
# 132203 too high
#  31568 correct