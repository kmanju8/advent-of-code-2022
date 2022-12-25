import re
import math
import time

def mine(blueprint, ore, robots, MINUTES, throttle, geodes, history):
    # we get 24 collection minutes
    if robots[0]>max(blueprint[0], blueprint[1], blueprint[2], blueprint[4]):
        return(0)

    if MINUTES<=0:
        return geodes

    best = geodes

    a = math.ceil((blueprint[0] - ore[0])/robots[0])
    b = math.ceil((blueprint[1] - ore[0])/robots[0])
    c = math.ceil(max((blueprint[2] - ore[0])/robots[0],(blueprint[3] - ore[1])/robots[1])) if robots[1]!=0 else 10000
    d = math.ceil(max((blueprint[4] - ore[0])/robots[0],(blueprint[5] - ore[2])/robots[2])) if robots[2]!=0 else 10000
    
    # turns for ore miner:
    options = [a,b,c,d]


    for count, TIME in enumerate(options):

        # start making it now. tick time down by one. ready for next minute
        if TIME<0:
            TIME = 0
        TIME+=1

        next_ore = [ore[i]+TIME*robots[i] for i in range(3)]

        # else takes 4 mins to save enough to build. robot ready one after
        if TIME<500:
            if count == 0:
                # next_ore = [ore[i]+TIME*robots[i] for i in range(3)]
                next_ore[0] -= blueprint[count]

                next_robots = robots.copy()
                next_robots[count] += 1

                m = mine(blueprint, next_ore, next_robots, MINUTES - TIME, throttle, geodes, history)
                best = max(best, m)

            elif count == 1:
                # next_ore = [ore[i]+TIME*robots[i] for i in range(3)]
                next_ore[0] -= blueprint[count]

                next_robots = robots.copy()
                next_robots[count] += 1

                m = mine(blueprint, next_ore, next_robots, MINUTES - TIME, throttle, geodes, history)
                best = max(best, m)
            elif count == 2:
                # next_ore = [ore[i]+TIME*robots[i] for i in range(3)]
                next_ore[0] -= blueprint[2]
                next_ore[1] -= blueprint[3]

                next_robots = robots.copy()
                next_robots[count] += 1

                m = mine(blueprint, next_ore, next_robots, MINUTES - TIME, throttle, geodes, history)
                best = max(best, m)
            elif count == 3:
                # next_ore = [ore[i]+TIME*robots[i] for i in range(3)]
                next_ore[0] -= blueprint[4]
                next_ore[2] -= blueprint[5]

                next_robots = robots.copy()

                a = history.copy()
                a.append((MINUTES,TIME))

                new_geodes = geodes+(MINUTES-TIME) if MINUTES-TIME>0 else geodes

                m = mine(blueprint, next_ore, next_robots, MINUTES - TIME, throttle, new_geodes, a)
                best = max(best, m)

    return best

MINUTES = 32

blueprints = {}
with open("inputp2.txt", "r") as f:
    for line in f:
        values = re.findall("\d+", line)
        blueprints[int(values[0])] = [int(i) for i in values[1:]]

ans = 1
start = time.time()
for i in blueprints:
    print(i)
    throttle = {}

    a = mine(blueprints[i], [0]*3, [1,0,0], MINUTES, throttle, 0, [])
    print(i, a, time.time()-start)
    ans *= a

print(ans)
