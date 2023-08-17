N = 7

g = [ list(map(int, input().split())) for _ in range(N) ]
g[0][0] = 1

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

cnt = 0
def dfs(y, x):
    global cnt
    if y == N - 1 and x == N - 1:
        cnt += 1
    else:
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and g[ny][nx] == 0:
                g[ny][nx] = 1
                dfs(ny, nx)
                g[ny][nx] = 0

dfs(0, 0)
print(cnt)
