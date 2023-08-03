from collections import deque

N, M = map(int, input().split())
a = [ (idx, val) for idx, val in enumerate(list(map(int, input().split())))]
a = deque(a)

cnt = 0
while True:
    cur = a.popleft()
    if any(cur[1] < x[1] for x in a):
        a.append(cur)
    else:
        cnt += 1
        if cur[0] == M:
            break

print(cnt)

