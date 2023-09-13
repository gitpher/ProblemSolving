from collections import deque

N = M = int(input())
field = [list(map(int, input())) for _ in range(N)]

res = []
visited = [[0] * M for _ in range(N)]

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

def bfs(y, x):
    dq = deque()
    dq.append((y, x))
    cnt = 1
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if is_valid_coord(ny, nx) and field[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                dq.append((ny, nx))
                cnt += 1
    return cnt

for i in range(N):
    for j in range(M):
        if field[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            res.append(bfs(i, j))

res.sort()
print(len(res))
for x in res:
    print(x)
