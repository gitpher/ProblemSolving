from collections import deque

def solution(priorities, location):
    
    dq = deque()
    
    for i in range(len(priorities)):
        dq.append((priorities[i], i))
    
    priorities.sort(reverse=True)
    
    i = 0
    while dq:
        cur = dq.popleft()
        if cur[0] == priorities[i]:
            i += 1
            if cur[1] == location:
                break
        else:
            dq.append(cur)
                
    return i
