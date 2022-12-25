x = 1
counter = 0
ans = 0

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip().split()

        match len(line):
            case 2:
                for i in range(2):
                    counter += 1
                    if counter%40 == 20:
                        ans += counter*x
                        print(counter, x)
                x += int(line[1])
            case other:
                counter += 1
                if counter%40 == 20:
                    ans += counter*x
                    print(counter, x)


print(ans, counter, x)

        