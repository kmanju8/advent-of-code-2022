import functools

def check(left:list, right:list) :
    for i in range(min(len(left),len(right))):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i]<right[i]:
                return (True, True)
            elif left[i]>right[i]:
                return (True,False)
        elif isinstance(left[i], int):
            mid = check([left[i]],right[i])
            if mid[0]:
                return mid
        elif isinstance(right[i], int):
            mid = check(left[i],[right[i]])
            if mid[0]:
                return mid
        else:
            mid = check(left[i],right[i])
            if mid[0]:
                return mid
    
    if len(left)>len(right):
        return (True, False)
    elif len(left)<len(right):
        return (True,True)
    return False, False

def make_comparator(check):
    def compare(left, right):
        if check(left, right)[1]:
            return -1
        elif check(right, left)[1]:
            return 1
        else:
            return 0

    return compare

codes = []
with open("inputp2.txt", 'r') as f:
    for line in f:
        codes.append(eval(line.strip()))

codes=sorted(codes,key=functools.cmp_to_key(make_comparator(check)))

print((codes.index([[2]])+1)*(codes.index([[6]])+1))

        
    
# print(ans)