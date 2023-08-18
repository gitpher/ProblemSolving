N = 10
g = [ list(map(int, input().split())) for _ in range(N) ]
chk = [ [0] * N for _ in range(N) ]

dy = (-1, 0, 0)
dx = (0, 1, -1)

def dfs(y, x):
    chk[y][x] = 1
    if y == 0:
        print(x)
    else:
        if x - 1 >= 0 and g[y][x - 1] == 1 and chk[y][x - 1] == 0:
            dfs(y, x - 1)
        elif x + 1 < N and g[y][x + 1] == 1 and chk[y][x + 1] == 0:
            dfs(y, x + 1)
        else:
            dfs(y - 1, x)

for j in range(N):
    if g[N -1][j] == 2:
        dfs(N - 1, j)
