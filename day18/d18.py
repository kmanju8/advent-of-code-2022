def inbounds(cube, canvasmin, canvasmax):
    for i in range(3):
        if cube[i]<(canvasmin[i]-1):
            return False

        if cube[i]>(canvasmax[i]+1):
            return False
    return True

def expand(gas, canvasmin, canvasmax, cubes, neigh, current):
    for dx, dy, dz in neigh:
        new_cube = (current[0] + dx, current[1] + dy, current[2] + dz)
        if (new_cube not in cubes) and (new_cube not in gas) and inbounds(new_cube, canvasmin, canvasmax):
            gas.add(new_cube)
            expand(gas, canvasmin, canvasmax, cubes, neigh, new_cube)

import sys
sys.setrecursionlimit(20000)

cubes = set()
canvasmin = [10000]*3
canvasmax = [-10000]*3

with open("input.txt", "r") as f:
    for line in f:
        cube = eval((line))
        cubes.add(cube)
        canvasmin = [min(canvasmin[i], cube[i]) for i in range(3)]
        canvasmax = [max(canvasmax[i], cube[i]) for i in range(3)]
        
ans = len(cubes) * 6

neigh = [
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1],
]

for cube in cubes:
    for dx, dy, dz in neigh:
        if (cube[0] + dx, cube[1] + dy, cube[2] + dz) in cubes:
            ans -= 1

print("lava cubes: ", len(cubes))
print("lava faces: ", ans)
# ans to part 1

# part 2
# randomly place cube on outside. spread to fill all area. add these cubes to own set. then count intersecting faces
start=tuple([i-1 for i in canvasmin])

gas = set([start])

expand(gas, canvasmin, canvasmax, cubes, neigh, start)

print("total gas cubes:", len(gas))

# count share faces with cubes
ans = 0

for g in gas:
    for dx, dy, dz in neigh:
        if (g[0] + dx, g[1] + dy, g[2] + dz) in cubes:
            ans += 1


print(ans)
