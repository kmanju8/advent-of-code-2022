import re
import time

def bfs(valves, start, end):
    visited = set()
     
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is
    # reached
    if start == end:
        print("Same Node")
        return
     
    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        # Condition to check if the
        # current node is not visited
        if node not in visited:
            neighbours = valves[node].neighbours
             
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == end:
                    # print("Shortest path = ", *new_path)
                    return len(new_path)-1
            visited.add(node)
 
    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting"\
                "path doesn't exist :(")
    return

def traverse(valves, currentflow, time, location, totalflow, open, throttle, cache, me):

    throttle[time]=max(throttle[time], totalflow-100)
    if totalflow < throttle[time+1]:
        return(0)
    # with 20s we hit 713 so can do below. how to generalise
    # if time<=10 and totalflow<trick-100:
    #     return 0
        
    if time == 0:
        if me:
            TIME2 = 26
            throttle2 = {i:0 for i in range(-5,TIME2+4)}
            # implement cache here
            past_visit = tuple(sorted(open))
            if past_visit not in cache:
                cache[past_visit] = traverse(valves, 0, TIME2, "AA", 0, open, throttle2, cache, False)
            return totalflow + cache[past_visit]
        return totalflow

    ans = totalflow
    # if we open valve at current location
    if location not in open and location != "AA":
        a = list(open)
        a.append(location)
        b = traverse(valves, currentflow + valves[location].flowrate, time-1, location, totalflow+currentflow, a, throttle, cache, me)
        ans = max(ans, b)

    for valve in valves[location].neighbours:
        if time-valves[location].neighbours[valve]>=0 and valve not in open:
            b = traverse(valves.copy(), currentflow, time-valves[location].neighbours[valve], valve, totalflow+currentflow*valves[location].neighbours[valve], open, throttle, cache, me)
            ans = max(ans, b)
        else:
            ans = max(ans, time*currentflow+totalflow)

    return ans

class Valve:
  def __init__(self, flowrate, neighbours):
    self.flowrate = flowrate
    self.neighbours = neighbours

valves = {}
no_flow={}
with open("input.txt", "r") as f:
    for line in f:
        connections = re.findall("[A-Z]{2}", line)
        rate = re.search("\d+", line)

        valves[connections[0]] = Valve(int(rate.group()), {i:1 for i in connections[1:]})
        if rate.group() == "0":
            no_flow[connections[0]] = {i:1 for i in connections[1:]}
            

# fuck it let's bfs everything:
new_graph = {}
for i in valves:
    temp = {}
    for j in valves:
        if i!=j and j not in no_flow:
            temp[j] = bfs(valves, i, j)
    new_graph[i] = temp
    
for name in valves:
    valves[name].neighbours = new_graph[name]

for name in no_flow:
    if name == "AA":
        continue
    del valves[name]

TIME = 26
throttle = {i:0 for i in range(-5,TIME+4)}

start = time.time()
cache = {}
a = traverse(valves, 0, TIME, "AA", 0, [], throttle, cache, True)
print(a)
# print(cache)

end = time.time()
print(end - start)