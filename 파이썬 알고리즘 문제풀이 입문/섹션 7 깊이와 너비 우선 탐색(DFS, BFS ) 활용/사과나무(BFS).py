from collections import deque

N = int(input())
g = [ list(map(int, input().split())) for _ in range(N) ]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
chk = [ [0] * N for _ in range(N) ]

mid = N // 2
chk[mid][mid] = 1
sum = g[mid][mid]

dq = deque()
dq.append((mid, mid))

lvl = 0
while True:
    if lvl == mid:
        break
    sz = len(dq)
    for i in range(sz):
        now = dq.popleft()
        for j in range(4):
            ny = now[0] + dy[j]
            nx = now[1] + dx[j]
            if chk[ny][nx] == 0:
                chk[ny][nx] = 1
                sum += g[ny][nx]
                dq.append((ny, nx))
    lvl += 1

print(sum)
