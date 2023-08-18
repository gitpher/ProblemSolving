N = int(input())
g = [ list(map(int, input().split())) for _ in range(N) ]

max_hgt = float('-inf')
for i in range(N):
    for j in range(N):
        if g[i][j] > max_hgt:
            max_hgt = g[i][j]

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

def dfs(y, x, h):
    chk[y][x] = 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and chk[ny][nx] == 0 and g[ny][nx] > h:
            dfs(ny, nx, h)


max_val = float('-inf')
for h in range(max_hgt + 1):
    cnt = 0
    chk = [ [0] * N for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            if g[i][j] > h and chk[i][j] == 0:
                dfs(i, j, h)
                cnt += 1
    if cnt > max_val:
        max_val = cnt

print(max_val)
