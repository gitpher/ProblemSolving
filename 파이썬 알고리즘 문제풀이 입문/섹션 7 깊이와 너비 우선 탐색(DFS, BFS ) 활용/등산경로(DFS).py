N = int(input())
g = [ list(map(int, input().split())) for _ in range(N) ]
chk = [ [0] * N for _ in range(N) ]

min_val = float('inf')
max_val = float('-inf')
min_pos = ()
max_pos = ()

for i in range(N):
    for j in range(N):
        if g[i][j] < min_val:
            min_val = g[i][j]
            min_pos = (i, j)
        if g[i][j] > max_val:
            max_val = g[i][j]
            max_pos = (i, j)

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

chk[min_pos[0]][min_pos[1]] = 1
cnt = 0
def dfs(y, x):
    global cnt
    if y == max_pos[0] and x == max_pos[1]:
        cnt += 1
    else:
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and chk[ny][nx] == 0 and g[ny][nx] > g[y][x]:
                chk[ny][nx] = 1
                dfs(ny, nx)
                chk[ny][nx] = 0

dfs(min_pos[0], min_pos[1])
print(cnt)
