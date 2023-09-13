import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
school = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, 1, -1)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

ans = 0

def dfs(y, x):
    global ans
    visited[y][x] = 1
    if school[y][x] == 'P':
        ans += 1
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if is_valid_coord(ny, nx) and visited[ny][nx] == 0 and school[ny][nx] != 'X':
            dfs(ny, nx)

for i in range(N):
    for j in range(M):
        if school[i][j] == 'I':
            dfs(i, j)
            break

print("TT" if ans == 0 else ans)
