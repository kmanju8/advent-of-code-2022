def winDraw(line):
    if (line[0]=="A" and line[2]=="Y") or (line[0]=="B" and line[2]=="Z") or (line[0]=="C" and line[2]=="X"):
        return 6
    if (line[0]=="A" and line[2]=="X") or (line[0]=="B" and line[2]=="Y") or (line[0]=="C" and line[2]=="Z"):
        return 3
    return 0

count = 0
val = {"X": 1, "Y": 2, "Z": 3}
with open('input.txt', 'r') as f:
    for line in f:
        count += val[line[2]]
        count += winDraw(line)
    
    print(count)


