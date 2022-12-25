def check(left:list, right:list) :
    for i in range(min(len(left),len(right))):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i]<right[i]:
                return 1
            elif left[i]>right[i]:
                return -1
        else:
            left[i] = [left[i]] if isinstance(left[i], int) else left[i]
            right[i] = [right[i]] if isinstance(right[i], int) else right[i]
            mid = check(left[i],right[i])
            if mid != 0:
                return mid
    
    # lists of diff length and order still undecided
    return(int(len(left)!=len(right))* (2*int(len(left)<len(right))-1))

# 3 scenarios : return a match (1), return a not-match (-1), or continue to check (0)

ans = 0
with open("input.txt", 'r') as file:
    index = 1
    while True:
        left = eval(file.readline().strip())
        right = eval(file.readline().strip())
        line = file.readline()

        if check(left,right)==1:
            print(index)
            ans += index    
        if not line:
            break
        
        index +=1

print(ans)
# 5717