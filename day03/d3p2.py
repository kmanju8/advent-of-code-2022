
score = {chr(i+96): i for i in range(1,27)}
capitals = {chr(i+38): i for i in range(27,53)}
score.update(capitals)

count = 0
with open('input.txt', 'r') as f:
    line_no = -1
    one = set()
    for l in f:
        line_no += 1
        line = l.strip()
        if line_no % 3 == 0:
            for i in line:
                one.add(i)
            one_two = set()
        if line_no % 3 == 1:
            for i in line:
                if i in one:
                    one_two.add(i)
        else:
            for i in line:
                if i in one_two:
                    count+=score[i]
                    one = set()
                    break
        

print(count)


