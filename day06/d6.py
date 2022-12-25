LENGTH = 14

with open('input.txt', 'r') as f:
    for code in f:  
        for i in range(len(code)-LENGTH):
            if len(set(code[i:i+LENGTH])) == LENGTH:
                print(i+LENGTH, code[i:i+LENGTH])
                break


            