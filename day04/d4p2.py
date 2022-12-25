count = 0

with open('input.txt', 'r') as f:
    for line in f:
        clean = [int(i) for i in line[:-1].replace(",", "-").split("-")]
        if (clean[0]<=clean[3] and clean[0]>=clean[2]) or (clean[1]<=clean[3] and clean[1]>=clean[2]) or (clean[3]<=clean[1] and clean[3]>=clean[0]) or (clean[2]<=clean[1] and clean[2]>=clean[0]):
            count += 1
            print(clean)

print(count)