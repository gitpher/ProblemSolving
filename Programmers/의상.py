def solution(clothes):
    
    a = dict(clothes)
    b = dict()
    
    for v in a.values():
        if v in b:
            b[v] += 1
        else:
            b[v] = 2
    
    cnt = 1
    for v in b.values():
        cnt *= v
    
    return cnt - 1
