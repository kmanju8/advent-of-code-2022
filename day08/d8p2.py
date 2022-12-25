trees = {}
counter = 0
with open('input.txt', 'r') as f:
  for line in f:
    for i, v in enumerate(line.strip()):
      trees[(i,counter)] = int(v)
    counter += 1
  LENGTH = len(line.strip())
visibility = {i: 1 for i in trees}

for tree in trees:
  for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
    i = 0
    in_bounds = tree[0]+dx*(i+1) >= 0 and tree[0]+dx*(i+1) < LENGTH and tree[1]+dy*(i+1) >= 0 and tree[1]+dy*(i+1) < LENGTH
    while in_bounds and trees[(tree[0]+dx*(i+1),tree[1]+dy*(i+1))] < trees[tree]:
      i += 1
      in_bounds = tree[0]+dx*(i+1) >= 0 and tree[0]+dx*(i+1) < LENGTH and tree[1]+dy*(i+1) >= 0 and tree[1]+dy*(i+1) < LENGTH
    i += 1 if in_bounds else 0
    visibility[tree] *= i

maximum = 0 
for i in visibility:
  maximum = max(visibility[i], maximum)

print(maximum)
  