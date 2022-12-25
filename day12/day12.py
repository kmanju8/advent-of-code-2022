# read map
elevation = {}
with open("input.txt", "r") as f:
    j=0
    for line in f:
        line = line.strip()
        for i,char in enumerate(line):
            elevation[(i,j)] = char
            if char == "S":
                start = (i,j)
                elevation[(i,j)] = "a"
            if char == "E":
                end = (i,j)
                elevation[(i,j)] = "z"
        j+=1

distance = {i:10000 for i in elevation}
distance[start] = 0
# part2
# for i in elevation:
#     if elevation[i]=="a":
#         distance[i]=0

visited = set()
need_to_visit = {}

current = start
while  current!=end:
    i, j = current
    visited.add((i,j))
    
    for dx, dy in ((0, 1), (0, -1), (-1,0),(1,0)):
        if (i+dx, j + dy) in elevation and ((i+dx, j + dy) not in visited):

            if  ord(elevation[(i, j)])+1 >= ord(elevation[(i + dx, j + dy)]) and (i+dx, j + dy) not in visited:
                distance[(i + dx, j + dy)] = min(distance[(i+dx, j + dy)], distance[(i,j)]+1)
                need_to_visit[(i + dx, j + dy)] = distance[(i + dx, j + dy)]

    current = min(need_to_visit, key=need_to_visit.get)
    del need_to_visit[current]
    # 381 too low
print(distance[current])
