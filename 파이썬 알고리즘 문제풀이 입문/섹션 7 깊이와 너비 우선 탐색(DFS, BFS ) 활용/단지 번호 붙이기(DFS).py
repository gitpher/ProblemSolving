N = int(input())
g = [ list(map(int, input())) for _ in range(N) ]

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

res = []

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

cnt = 0
def dfs(y, x):
    global cnt
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and g[ny][nx] == 1:
            g[ny][nx] = 0
            cnt += 1
            dfs(ny, nx)

for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            g[i][j] = 0
            cnt += 1
            dfs(i, j)
            res.append(cnt)
            cnt = 0

print(len(res))
for x in res:
    print(x)
