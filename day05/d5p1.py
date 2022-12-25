stacks = {
    1: ["V","Q","W","M","B","N","Z","C"],
    2: ["B","C","W","R","Z","H"],
    3: ["J","R","Q","F"],
    4: ["T","M","N","F","H","W","S","Z"],
    5: ["P","Q","N","L","W","F","G"],
    6: ["W","P","L"],
    7: ["J","Q","C","G","R","D","B","V"],
    8: ["W","B","N","Q","Z"],
    9: ["J","T","G","C","F","L","H"],
}
for i in stacks:
    stacks[i].reverse()

with open('input.txt', 'r') as f:
    for line in f:
        clean = [int(i) for i in line[:-1].replace("from", "to").split("to")]
        # for part 1, swap l20 with 21
        # stacks[clean[2]] += stacks[clean[1]][-clean[0]:][::-1]
        stacks[clean[2]] += stacks[clean[1]][-clean[0]:]
        stacks[clean[1]] = stacks[clean[1]][0:(-clean[0])]

for i in range(1,10):
    print(stacks[i][-1])