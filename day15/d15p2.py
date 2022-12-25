# def merge(intervals):
#     if len(intervals) == 0 or len(intervals) == 1:
#         return intervals
#     intervals.sort(key=lambda x:x[0])
#     result = [intervals[0]]
#     for interval in intervals[1:]:
#         if interval[0] <= result[-1][1]:
#             result[-1][1] = max(result[-1][1], interval[1])
#         else:
#             result.append(interval)
#     return result

# RANGE = 4000000
# # RANGE = 20
# # PLANE = 10
# checks = set()

# intervals = []
# with open("input.txt", "r") as f:
#     for line in f:
#         line = line.strip().split()
#         sensor = [int(line[2][2:-1]),int(line[3][2:-1])]
#         beacon = [int(line[8][2:-1]),int(line[9][2:])]

#         distance = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])

#         for i in range(distance+2):
#             x,y = sensor[0]+i,(sensor[1]+distance+1)-i
#             if x>0 and x<=RANGE and y>0 and y<=RANGE:
#                 checks.add((x,y))

#             x,y = sensor[0]+i,(sensor[1]-distance-1)+i
#             if x>0 and x<RANGE and y>0 and y<RANGE:
#                 checks.add((x,y))
            
#             x,y = sensor[0]-i,(sensor[1]-distance-1)+i
#             if x>0 and x<RANGE and y>0 and y<RANGE:
#                 checks.add((x,y))

#             x,y = sensor[0]-i,(sensor[1]+distance+1)-i
#             if x>0 and x<RANGE and y>0 and y<RANGE:
#                 checks.add((x,y))

#         intervals.append([sensor[0],sensor[1], distance])

# for point in checks:
#     check = False
#     for interval in intervals:
#         if (abs(point[0]-interval[0])+abs(point[1]-interval[1]))<=interval[2]:
#             check = True
#             break
#     if not check:
#         print(point)


# (2706598, 3253551)

print(4000000*2706598+ 3253551)
