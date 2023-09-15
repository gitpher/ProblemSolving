import sys
sys.setrecursionlimit(10**7)

N, M, K = map(int, input().split())
grid = [[0] * M for _ in range(N)]
rectangles = [list(map(int, input().split())) for _ in range(K)]

for rect in rectangles:
    for i in range(rect[1], rect[3]):
        for j in range(rect[0], rect[2]):
            grid[i][j] = 1

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

res = []
cnt = 0
def dfs(y, x):
    global cnt
    cnt += 1
    grid[y][x] = 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and grid[ny][nx] == 0:
            dfs(ny, nx)

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            dfs(i, j)
            res.append(cnt)
            cnt = 0

print(len(res))
for x in sorted(res):
    print(x, end=' ')
