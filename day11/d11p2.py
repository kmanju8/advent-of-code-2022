counter = {i: 0 for i in range(8)}
FACTOR = 13 * 19 * 5 * 2 * 17 * 11 * 7 * 3

monkeys = {
    0: [64],
    1: [60, 84, 84, 65],
    2: [52, 67, 74, 88, 51, 61],
    3: [67, 72],
    4: [80, 79, 58, 77, 68, 74, 98, 64],
    5: [62, 53, 61, 89, 86],
    6: [86, 89, 82],
    7: [92, 81, 70, 96, 69, 84, 83],
}

ops = [
    lambda x: x * 7,
    lambda x: x + 7,
    lambda x: x * 3,
    lambda x: x + 3,
    lambda x: x * x,
    lambda x: x + 8,
    lambda x: x + 2,
    lambda x: x + 4,
]

tests = [
    lambda x: 1 if x % 13 == 0 else 3,
    lambda x: 2 if x % 19 == 0 else 7,
    lambda x: 5 if x % 5 == 0 else 7,
    lambda x: 1 if x % 2 == 0 else 2,
    lambda x: 6 if x % 17 == 0 else 0,
    lambda x: 4 if x % 11 == 0 else 6,
    lambda x: 3 if x % 7 == 0 else 0,
    lambda x: 4 if x % 3 == 0 else 5,
]

for i in range(10000):
    if i % 500 == 0:
        print(i)

    for monkey in range(8):
        for item in monkeys[monkey]:
            # worry = int(ops[monkey](item)/3)
            worry = int(ops[monkey](item) % FACTOR)
            monkeys[tests[monkey](worry)].append(worry)
        counter[monkey] += len(monkeys[monkey])
        monkeys[monkey] = []

a = list(counter.values())
a.sort()
print(a[-1] * a[-2])
