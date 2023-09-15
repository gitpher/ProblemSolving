from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dq = deque(enumerate(map(int, input().split())))
    cnt = 0
    while dq:
        mx = max(val for _, val in dq)
        idx, val = dq.popleft()

        if val != mx:
            dq.append((idx, val))
            continue

        cnt += 1

        if idx == M:
            print(cnt)
            break
