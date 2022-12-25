import re
import math
import time

def mine(blueprint, ore, robots, MINUTES, throttle, geodes, history):
    # we get 24 collection minutes
    # print(robots)
    if robots[0]>max(blueprint[0], blueprint[1], blueprint[2], blueprint[4]):
        return(0)

    if MINUTES<=0:
        # if geodes==7:

        #     print(robots, geodes, history)
        # if geodes>9:
        # if robots == [1,4,4]:
        #     print(robots, geodes, ore)
        return geodes

    best = geodes
# 1/2
    a = math.ceil((blueprint[0] - ore[0])/robots[0])
    b = math.ceil((blueprint[1] - ore[0])/robots[0])
    c = math.ceil(max((blueprint[2] - ore[0])/robots[0],(blueprint[3] - ore[1])/robots[1])) if robots[1]!=0 else 10000
    d = math.ceil(max((blueprint[4] - ore[0])/robots[0],(blueprint[5] - ore[2])/robots[2])) if robots[2]!=0 else 10000
    

    
    # turns for ore miner:
    options = [a,b,c,d]
    # print(options)



    for count, TIME in enumerate(options):

        # start making it now. tick time down by one. ready for next minute
        if TIME<0:
            TIME = 0
        TIME+=1

        next_ore = [ore[i]+TIME*robots[i] for i in range(3)]

        # else takes 4 mins to save enough to build. robot ready one after
        if TIME<500:
            if count == 0 or count == 1:
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




MINUTES = 24

blueprints = {}
with open("input.txt", "r") as f:
    for line in f:
        values = re.findall("\d+", line)
        blueprints[int(values[0])] = [int(i) for i in values[1:]]


ans = 0
start = time.time()
for i in blueprints:
    print(i)
    throttle = {}

    a = mine(blueprints[i], [0]*3, [1,0,0], MINUTES, throttle, 0, [])
    print(i, a, time.time()-start)
    ans += i*a

print(ans)
end = time.time()
print("time taken:", end - start)




# print(ans)
# 15960 too low, close as right answer for someone else
# 16530 also too low
# 16800 too low
# 17052 not right (28 21 29)
# 19968 not right
# 28*19*32

# not 28*21*32

# bests
# 1: 28 with throttle -10
# 2: 21 with throttle -10
# 3: 31 with throttle -14

# 28*21*31


# 26 15 31


# example file
# 1 - add eode miners at min 6 and 3
# in slow is the same -  6 and 3

# 2 - add geode miners in mins 5 and 2
# in slow (6&3, wrong anyway)

# [('ore', 22), technically 21
# ('ore', 20), technically 19
#  ('clay', 19), 
# ('clay', 18), 
# ('clay', 17), 
# ('clay', 16), 
# ('clay', 15), 
# ('obsidean', 14), 
# ('clay', 14), 
# ('obsidean', 13), 
# ('obsidean', 12), 
# ('obsidean', 11),
#  ('obsidean', 10), 
# ('obsidean', 8), 
# ('geode', 7),
#  ('obsidean', 6),
#  ('geode', 5), 
# ('obsidean', 4), 
# ('clay', 4),
#  ('geode', 3),
#  ('obsidean', 2)]