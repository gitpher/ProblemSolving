from collections import deque

S = input()
N = int(input())

for i in range(N):
    dq = deque(S)
    for ch in input():
        if ch in dq:
            if ch != dq.popleft():
                print(f'#{i + 1} NO')
                break
    else:
        if len(dq) == 0:
            print(f'#{i + 1} YES')
        else: # 순서대로 필수교육과정이 있었지만 다 있지는 않았을 수 있음
            print(f'#{i + 1} NO')
            
