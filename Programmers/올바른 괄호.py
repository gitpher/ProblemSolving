def solution(s):
    
    a = list()
    
    for x in s:
        if x == '(':
            a.append(x)
        else:
            if a:
                a.pop()
            else:
                return False
    
    return False if a else True
