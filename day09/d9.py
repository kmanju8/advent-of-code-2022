# change length to 2 for part 1
LENGTH = 10
visited = set()
visited.add((0,0))
directions = {"U": (0, 1), "D": (0, -1), "L": (-1,0), "R": (1,0)}
rope = [[0,0] for i in range(LENGTH)]

with open("input.txt", "r") as f:
    inst=0
    for line in f:
        line = line.strip().split()
        for i in range(int(line[1])):
            next_rope = [[rope[0][0] + directions[line[0]][0], rope[0][1] + directions[line[0]][1]]] + [[0,0]]*(LENGTH-1)
            for j in range(1, LENGTH):
                # rope segment doesn't move
                if abs(rope[j][0]-next_rope[j-1][0])<2 and abs(rope[j][1]-next_rope[j-1][1])<2 :
                    next_rope[j:] = rope[j:]
                    break
                # rope segment moves
                else:
                    # horizonal movement
                    if rope[j][0]==next_rope[j-1][0] or rope[j][1]==next_rope[j-1][1]:
                        if rope[j][0]==next_rope[j-1][0]:
                            next_rope[j] = [rope[j][0],int((rope[j][1]+next_rope[j-1][1])/2)]
                        else:
                            next_rope[j] = [int((rope[j][0]+next_rope[j-1][0])/2), rope[j][1]]
                    # vertical movement
                    else:                    
                        move = [int(v/abs(v)) for v in [next_rope[j-1][z]-rope[j][z] for z in range(2)]]
                        next_rope[j] = [rope[j][a]+move[a] for a in range(2)]

            rope = next_rope
            
            visited.add(tuple(rope[-1]))
        inst+=1

print(len(visited))
