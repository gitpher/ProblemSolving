from collections import deque

S = input()
N = int(input())

for i in range(N):
    dq = deque(S)
    for j in input():
        if j in dq:
            dq.popleft()
    if len(dq) == 0:
        print(f'#{i+1} YES')
    else:
        print(f'#{i + 1} NO')

