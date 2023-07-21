for _ in range(int(input())):
    stk = []
    isVPS = True
    
    for ch in input():
        if ch == '(':
            stk.append(ch)
        else:
            if len(stk) > 0 :
                stk.pop()
            else:
                isVPS = False
                break
    
    if len(stk) > 0:
        isVPS = False
    
    print('YES' if isVPS == True else 'NO')
