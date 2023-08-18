from collections import deque

M, N = map(int, input().split())
g = [ list(map(int, input().split())) for _ in range(N) ]
chk = [ [0] * M for _ in range(N) ]

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M # 0 <= x < N이 아니라 0 <= x < M임

dq = deque()
for i in range(N):
    for j in range(M):
        if g[i][j] == 1:
            dq.append((i, j))

while dq:
    y, x = dq.popleft()
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and g[ny][nx] == 0:
            g[ny][nx] = 1
            chk[ny][nx] = chk[y][x] + 1
            dq.append((ny, nx))

is_all_ripe = True
max_val = 0
for i in range(N):
    for j in range(M):
        if g[i][j] == 0:
            is_all_ripe = False
            break
        if chk[i][j] > max_val:
            max_val = chk[i][j]

if is_all_ripe:
    print(max_val)
else:
    print(-1)
