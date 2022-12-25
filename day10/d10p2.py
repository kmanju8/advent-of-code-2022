x = 1
counter = -1
output = ""

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip().split()

        match len(line):
            case 2:
                for i in range(2):
                    counter += 1
                    output += "#" if counter%40 in [x-1,x,x+1] else "."
                    if (counter+1)%40 == 0:
                        print(output)
                        output = ""
                x += int(line[1])
            case other:
                counter += 1
                output += "#" if counter%40 in [x-1,x,x+1] else "."
                if (counter+1)%40 == 0:
                    print(output)
                    output = ""

        