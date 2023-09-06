from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    br = deque([0] * bridge_length)
    tr = deque(truck_weights)
    
    cnt = 0
    tot = 0
    while tr:
        cnt += 1
        tot -= br.popleft()
        
        if tot + tr[0] <= weight:
            cur = tr.popleft()
            br.append(cur)
            tot += cur
        else:
            br.append(0)
               
    return cnt + bridge_length
