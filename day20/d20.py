class Value:
    def __init__(self, value):
        self.value = value
        self.location = value


def make_reg(o, value, length):
    # let's just do if too big first
    

    # if o+value == 0 or o+value == length-1:
    #     return length
    if o+value == 0:
        return 0
    elif o+value == length-1:
        return length
    elif (o+value>=0 and o+value<length):
        return(o+value)
    else: 
        # o+value == length-1 too big
        return make_reg(((o+value)%length)+((o+value)//length), 0 ,length)
        
    # if o+valuemap[i]>length:
    #     n = ((o+valuemap[i])%length)+((o+valuemap[i])//length)
    # elif o+valuemap[i]<0:
    #     # print((o+valuemap[i])//length)
    #     n = ((o+valuemap[i])%length)+((o+valuemap[i])//length)
    # elif o+valuemap[i] == 0:
    #     a = codes.pop(o)
    #     codes.append(a)
    #     continue
    # elif o+valuemap[i] == length-1:
    #     a = codes.pop(o)
    #     codes.append(a)
    #     # codes = [a]+codes
    #     continue


KEY = 811589153
codes = []
valuemap = {}
with open("input.txt", "r") as f:
    count = 0
    for line in f:
        codes.append(count)
        valuemap[count] = int(line)*KEY
        count += 1

length = len(codes)
# print(length)
# give everything codenames in a map


for x in range(10):
    for i in range(length):
        o = codes.index(i)
        n = make_reg(o, valuemap[i], length)
        codes.insert(n, codes.pop(o))
        # ans = [valuemap[i] for i in codes]
        # print(valuemap[i], ans)
    print([valuemap[i] for i in codes])

# for x in range(1):
#     for i in range(length):
#         o = codes.index(i)
#         if o+valuemap[i]>length:
#             n = ((o+valuemap[i])%length)+((o+valuemap[i])//length)
#         elif o+valuemap[i]<0:
#             # print((o+valuemap[i])//length)
#             n = ((o+valuemap[i])%length)+((o+valuemap[i])//length)
#         elif o+valuemap[i] == 0:
#             a = codes.pop(o)
#             codes.append(a)
#             continue
#         elif o+valuemap[i] == length-1:
#             a = codes.pop(o)
#             codes.append(a)
#             # codes = [a]+codes
#             continue
#         else:
#             n = (o+valuemap[i])
#         codes.insert(n, codes.pop(o))
#         # ans = [valuemap[i] for i in codes]
#         # print(valuemap[i], ans)
#     print([valuemap[i] for i in codes])

ans = [valuemap[i] for i in codes]
z = ans.index(0)
# print(z)

print(ans[(z+1000)%length], ans[(z+2000)%length], ans[(z+3000)%length])
print(ans[(z+1000)%length]+ans[(z+2000)%length]+ans[(z+3000)%length])
# correct is 7228

# print(ans)

# only if moves forward
# for i in codes:
#     old = i.location
#     new = i.location + i.value
#     if new>length:
#         new %= length
#     for k in codes:
#         if k.location in range(old+1, new+1):
#             k.location -= 1
#     i.location = new

# Initial arrangement:
# 1, 2, -3, 3, -2, 0, 4

# 1 moves between 2 and -3:
# 2, 1, -3, 3, -2, 0, 4

# 2 moves between -3 and 3:
# 1, -3, 2, 3, -2, 0, 4

# -3 moves between -2 and 0:
# 1, 2, 3, -2, -3, 0, 4

# 3 moves between 0 and 4:
# 1, 2, -2, -3, 0, 3, 4

# -2 moves between 4 and 1:
# 1, 2, -3, 0, 3, 4, -2

# 0 does not move:
# 1, 2, -3, 0, 3, 4, -2

# 4 moves between -3 and 0:
# 1, 2, -3, 4, 0, 3, -2