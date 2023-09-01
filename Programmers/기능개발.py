from collections import deque

def solution(progresses, speeds):
    
    res = list()
    p = deque(progresses)
    s = deque(speeds)
    
    while p:
        for i in range(len(p)):
            p[i] += s[i]
        
        cnt = 0
        while p and p[0] >= 100:
            p.popleft()
            s.popleft()
            cnt += 1
        
        if cnt > 0:
            res.append(cnt)
            
    return res
