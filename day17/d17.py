landed = set([(i,0) for i in range(7)])

with open("input.txt", "r") as f:
    for line in f:
        pattern = line.strip()

# x coords all between 0 and 6 (inclusive)

rocks = [
    [[0,0],[1,0],[2,0],[3,0]],
    [[1,0],[0,1],[2,1],[1,2],[1,1]],
    [[0,0],[1,0],[2,0],[2,1],[2,2]],
    [[0,0],[0,1],[0,2],[0,3]],
    [[0,0],[1,0],[0,1],[1,1]]
]
current_rock = 0
current_pattern = 0
pattern_length = len(pattern)

# print(pattern, len(pattern))

max_height = 0
corner = [2,max_height+4]

ROCKO = 6870

# repeats every 1715 rocks
# 0 0 0
# 1725 15 0
# 3440 15 0
# 5155 15 0
# 6870 15 0
# 8585 15 0
# rocko/

# print(int(1000000000000/1715), 1000000000000%1715)
# print(166*int(ROCKO/100)-26)
for i in range(ROCKO):
    while True:
        if current_pattern==15:
            print(i, current_pattern, current_rock)
            
        if pattern[current_pattern]=="<":
            next_rock = [corner[0]-1, corner[1]]
        else:
            next_rock = [corner[0]+1, corner[1]]
            
        change = True
        for dx,dy in rocks[current_rock]:
            # if all of these are valid
            if not ((next_rock[0]+dx,next_rock[1]+dy) not in landed and next_rock[0]+dx>=0 and next_rock[0]+dx<7):
                change = False
        if change:
            corner = next_rock

        current_pattern=(current_pattern+1)%pattern_length




        change = False
        next_rock = [corner[0], corner[1]-1]
        for dx,dy in rocks[current_rock]:
            if (next_rock[0]+dx,next_rock[1]+dy) in landed:
                # print(corner, next_rock)
                # print(next_rock[0]+dx,next_rock[1]+dy)
                change = True
        if change:
            for dx,dy in rocks[current_rock]:
                if corner[1]+dy > max_height:
                    max_height =  corner[1]+dy
                landed.add((corner[0]+dx,corner[1]+dy))
            corner = [2,max_height+4]
            break
        
        corner=next_rock

    # if current_pattern==4 and current_rock==0:
    
    current_rock = (current_rock+1)%5

print(ROCKO, "******", max_height)

# print(landed-set([(i,0) for i in range(7)]))

# 2919 too low
# canvas = []
# for i in range(max_height+1):
#     canvas.append(["."]*7)

# for i in landed:
#     canvas[i[1]][i[0]]="#"

# canvas.reverse()
# for i in canvas:
#     print(i)

# part 2 mostly done with some analytics, tweaking, and linear interpolation