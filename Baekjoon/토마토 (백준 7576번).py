from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dq = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            dq.append((i, j))

visited = [[False] * M for _ in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

while dq:
    y, x = dq.popleft()
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and not visited[ny][nx] and board[ny][nx] == 0:
            visited[ny][nx] = True
            board[ny][nx] = board[y][x] + 1
            dq.append((ny, nx))

has_unripe = False
ans = 0
for i in range(N):
    ans = max(ans, max(board[i]))
    for j in range(M):
        if board[i][j] == 0:
            has_unripe = True
            break

print(-1) if has_unripe else print(ans - 1)
