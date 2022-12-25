# Parsing, store in dictionary ig

trees = {}
counter = 0
with open('input.txt', 'r') as f:
  for line in f:
    for i, v in enumerate(line[:-1]):
      trees[(i,counter)] = int(v)
    counter += 1

visible = {}
# 4 passes, on win each direction.

for j in range(99):
  lr = -1 #maybe -1
  last_high_lr = 0
  rl = -1
  last_high_rl = 0

  for i in range(99):
    if trees[(i,j)]  > lr:
      if (i,j) not in visible:
        visible[(i,j)] = i - last_high_lr
      else:
        visible[(i,j)] *= i - last_high_lr
      lr = trees[(i,j)]
      last_high_lr = i

    if trees[(98-i,j)]  > rl:
      if (98-i,j) not in visible:
        visible[(98-i,j)] = i - last_high_rl
      else:
        visible[(98-i,j)] *= i - last_high_rl
      rl = trees[(98-i,j)]
      last_high_lr = i

  # now do the same but r to l (within j loop)

for i in range(99):
  lr = -1 #maybe -1
  last_high_lr = 0
  rl = -1
  last_high_rl = 0

  for j in range(99):
    if trees[(i,j)]  > lr:
      if (i,j) not in visible:
          visible[(i,j)] = j - last_high_lr
      else:
        visible[(i,j)] *= j - last_high_lr
      lr = trees[(i,j)]
      last_high_lr = j

    if trees[(i,98-j)]  > rl:
      if (i,98-j) not in visible:
        visible[(i,98-j)] = j - last_high_rl
      else:
        visible[(i,98-j)] *= j - last_high_rl
      rl = trees[(i,98-j)]
      last_high_rl = j


print(len(visible))

maximum = 0
for i in visible:
  maximum = max(visible[i], maximum)

print(maximum)