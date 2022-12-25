import re

values = {}
operations = {}
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip().split()
        # blueprints[int(values[0])] = [int(i) for i in values[1:]]
        if len(line)==2:
            values[line[0][:-1]] = int(line[1])
        else:
            operations[line[0][:-1]] = line[1:]

operations["root"][1] = "=="
values["humn"] = 3349136384441
# literally kinda guessed this one.
# Line XX is key, shows me final calculation for "root"'s compared value

# a = set(["humn"])

while len(operations)>0:

    # move operations to values whilst calculating real values
    for calc in operations:
        x = operations[calc][0]
        y = operations[calc][2]
        operator = operations[calc][1]
        if x in values and y in values:
            if calc == "root":
                print(x, values[x],y, values[y], values[y]/values[x])
            values[calc] = eval(str(values[x])+operator+str(values[y]))

    # sweep through values. If in operations, del from operations
    for value in values:
        if value in operations:
            del operations[value]

print(values["root"])
