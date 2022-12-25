def winDraw(line):
    mapping = {"A": 0, "B": 1, "C": 2}
    mapping2 = {"X": -1, "Y": 0, "Z": 1}
    score = [1,2,3]
    return score[(mapping[line[0]]+mapping2[line[2]])%3]

count = 0
val = {"X": 0, "Y": 3, "Z": 6}
with open('input.txt', 'r') as f:
    for line in f:
        count += val[line[2]]
        count += winDraw(line)
    
    print(count)


