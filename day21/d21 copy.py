import re

values = {}
operations = {}
with open("input2.txt", "r") as f:
    for line in f:
        line = line.strip().split()
        # blueprints[int(values[0])] = [int(i) for i in values[1:]]
        if len(line)==2:
            values[line[0][:-1]] = int(line[1])
        else:
            operations[line[0][:-1]] = line[1:]


while len(operations)>0:

    # move operations to values whilst calculating real values
    for calc in operations:
        x = operations[calc][0]
        y = operations[calc][2]
        operator = operations[calc][1]
        if x in values and y in values:
            values[calc] = eval(str(values[x])+operator+str(values[y]))

    # sweep through values. If in operations, del from operations
    for value in values:
        if value in operations:
            del operations[value]

print(values["root"])