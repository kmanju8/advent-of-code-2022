dir = {
    ">": (1, 0),
    "<": (-1, 0),
    "v": (0, 1),
    "^": (0, -1),
}

# progress-blizzard takes a set of blizzard coordinates, and returns the blizzard in the next turn
def progress_blizzard(grid, can_step, width, height):
    next_blizz = set()
    for tile in grid:
        next_tile = [tile[0] + dir[tile[2]][0], tile[1] + dir[tile[2]][1]]
        # wrap around
        if tuple(next_tile) not in can_step:
            if next_tile[0] == width - 1:
                next_tile[0] = 1
            elif next_tile[0] == 0:
                next_tile[0] = width - 2
            elif next_tile[1] == 0:
                next_tile[1] = height - 2
            elif next_tile[1] == height-1:
                next_tile[1] = 1
            else:
                print("oh fuck")
        next_blizz.add((next_tile[0],next_tile[1], tile[2]))

    return(next_blizz)

def traverse(start, end, blizzard, can_step):

    walks = [
        [0,0],
        [1,0],
        [-1,0],
        [0,1],
        [0,-1],
    ]

    # blizzard procession followed by DFS
    queue = set()  # Initialize a queue
    next_queue = set()

    # function for BFS
    queue.add(start)
    turn=0

    while end not in queue:          
        # turn counter in here
        blizzard = progress_blizzard(blizzard, can_step, width, height)
        blizz_tiles = set([(tile[0],tile[1]) for tile in blizzard])

        for position in queue:
            # check walkable location
            for walk in walks:
                test_step = (position[0]+walk[0],position[1]+walk[1])
                if test_step in can_step:
                    if test_step not in blizz_tiles:
                            next_queue.add(test_step)

        queue = next_queue
        next_queue = set()
        turn += 1
    return(turn)

blizzard = set()
can_step = set()
with open("input.txt", "r") as f:
    height = 0
    for line in f:
        line = line.strip()
        for i in range(len(line)):
            if line[i] != "#":
                can_step.add((i, height))

            if line[i] != "." and line[i] != "#":
                blizzard.add((i, height, line[i]))
        width = len(line)
        height += 1

a=traverse((1, 0),(width-2,height-1), blizzard, can_step)
b=traverse((width-2,height-1),(1, 0), blizzard, can_step)
c=traverse((1, 0),(width-2,height-1), blizzard, can_step)

print(a+b+c)