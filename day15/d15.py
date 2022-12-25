def merge(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x:x[0])
    result = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result

PLANE = 2000000
# PLANE = 10

intervals = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip().split()
        sensor = [int(line[2][2:-1]),int(line[3][2:-1])]
        beacon = [int(line[8][2:-1]),int(line[9][2:])]

        distance = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])

        if sensor[1]>PLANE-distance and sensor[1]<PLANE+distance:
            x_len = distance-abs(sensor[1]-PLANE)
            a = [sensor[0]-(x_len),sensor[0]+(x_len)]
            intervals.append(a)

sorted_intervals = merge(intervals)
print(intervals)
print(sorted_intervals)

ans = 0
for i in sorted_intervals:
    ans += (i[1]-i[0])

print(ans)
# 4793063 too high