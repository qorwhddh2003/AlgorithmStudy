import sys

T = int(sys.stdin.readline())

for _ in range(T) : 
        
    stack = []
    tf = True

    for s in list(sys.stdin.readline()) :     

        if s  == '(' :  
            stack.append('(')
        elif s == ')' : 
            if len(stack) == 0 : 
                tf = False
                break
            else :
                stack.pop()

    
    print('YES' if tf and len(stack) == 0 else 'NO')