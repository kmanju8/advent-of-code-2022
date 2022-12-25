
score = {chr(i+96): i for i in range(1,27)}
capitals = {chr(i+38): i for i in range(27,53)}
score.update(capitals)

count = 0
with open('input.txt', 'r') as f:
    for l in f:
        line = l.strip()
        checker = set()
        n = len(line) // 2
        for i in range(n):
            checker.add(line[i])
        for i in range(n):
            if line[-i-1] in checker:
                count += score[line[-i-1]]
                break

print(count)


