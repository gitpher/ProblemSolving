from collections import deque

N = int(input())
g = [ list(map(int, input().split())) for _ in range(N) ]

dy = (-1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, 1, 1, 1, 0, -1, -1, -1)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

dq = deque()
def bfs(y, x):
    dq.append((y, x))
    while dq:
        y, x = dq.popleft()
        for k in range(8):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and g[ny][nx] == 1:
                g[ny][nx] = 0
                dq.append((ny, nx))

cnt = 0
for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            g[i][j] = 0
            bfs(i, j)
            cnt += 1

print(cnt)
