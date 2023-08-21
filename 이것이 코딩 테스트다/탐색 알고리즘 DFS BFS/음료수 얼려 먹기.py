N, M = map(int, input().split())
g = [ list(map(int, input())) for _ in range(N) ]

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def dfs(y, x):
    g[y][x] = 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and g[ny][nx] == 0:
            dfs(ny, nx)

cnt = 0
for i in range(N):
    for j in range(M):
        if g[i][j] == 0:
            dfs(i, j)
            cnt += 1

print(cnt)
