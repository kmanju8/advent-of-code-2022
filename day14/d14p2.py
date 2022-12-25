rocks = set()
with open("inputp2.txt", "r") as f:
    for line in f:
        line = [[int(j) for j in i.split(",")] for i in line.strip().split(" -> ")]

        for point in line:
            rocks.add(tuple(point))

        for i in range(1,len(line)):
            if line[i][0]==line[i-1][0]:
                for j in range(min(line[i][1],line[i-1][1])+1,max(line[i][1],line[i-1][1])):
                    rocks.add((line[i][0],j))
            else:
                for j in range(min(line[i][0],line[i-1][0])+1,max(line[i][0],line[i-1][0])):
                    rocks.add((j,line[i][1]))

rockno = len(rocks)

current_rock = [500,0]
while True:
    if tuple([current_rock[0], current_rock[1]+1]) not in rocks:
        current_rock[1] += 1
    elif tuple([current_rock[0]-1, current_rock[1]+1]) not in rocks:
        current_rock[0] -= 1
        current_rock[1] += 1
    elif tuple([current_rock[0]+1, current_rock[1]+1]) not in rocks:
        current_rock[0] += 1
        current_rock[1] += 1
    else:
        rocks.add(tuple(current_rock))
        if tuple(current_rock) == (500,0):
            break
        current_rock = [500,0]

print(len(rocks)-rockno)

# 165 is lowest rock, so will add huge plane to 167