count = 0

with open('input.txt', 'r') as f:
    for line in f:
        clean = [int(i) for i in line[:-1].replace(",", "-").split("-")]
        if (clean[0]<=clean[2] and clean[1]>=clean[3]) or (clean[0]>=clean[2] and clean[1]<=clean[3]):
            count += 1

print(count)