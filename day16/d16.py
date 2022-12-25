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

def traverse(valves, currentflow, time, location, totalflow, open, throttle):

    throttle[time]=max(throttle[time], totalflow-20)
    if totalflow < throttle[time]:
        return(0)
    # with 20s we hit 713 so can do below. how to generalise
    # if time<=15 and totalflow<500:
    #     return 0
        
    if time == 0:
        return totalflow

    if len(open)==15:
        return totalflow + currentflow*time

    ans = totalflow
    # if we open valve at current location
    if location not in open:
        a = list(open)
        a.append(location)
        b = traverse(valves, currentflow + valves[location].flowrate, time-1, location, totalflow+currentflow, a, throttle)
        ans = max(ans, b)

    for valve in valves[location].neighbours:
        if time-valves[location].neighbours[valve]>=0 and valve not in open:
            b = traverse(valves.copy(), currentflow, time-valves[location].neighbours[valve], valve, totalflow+currentflow*valves[location].neighbours[valve], open, throttle)
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
# flowing_valves = 0
with open("input.txt", "r") as f:
    for line in f:
        connections = re.findall("[A-Z]{2}", line)
        rate = re.search("\d+", line)

        valves[connections[0]] = Valve(int(rate.group()), {i:1 for i in connections[1:]})
        if rate.group() == "0":
            no_flow[connections[0]] = {i:1 for i in connections[1:]}
            

# let's bfs everything:
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

# for i in valves:
#     print(i, valves[i].neighbours)
print(len(valves))
# for i in range(10,20):
TIME = 30
throttle = {i:0 for i in range(-10,TIME+1)}

start = time.time()
a = traverse(valves, 0, TIME, "AA", 0, [], throttle)
print(a)

end = time.time()
print(end - start)
# ans 1728
