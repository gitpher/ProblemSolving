from collections import deque

N = int(input())
graph = []
max_height = 0
for _ in range(N):
    row = list(map(int, input().split()))
    max_height = max(max_height, max(row))
    graph.append(row)

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def bfs(y, x, limit, visited):
    dq = deque()
    dq.append((y, x))
    visited[y][x] = True
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] > limit and not visited[ny][nx]:
                visited[ny][nx] = True
                dq.append((ny, nx))

max_count = 0
for limit in range(max_height):
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] > limit and not visited[i][j]:
                bfs(i, j, limit, visited)
                cnt += 1

    max_count = max(max_count, cnt)

print(max_count)
