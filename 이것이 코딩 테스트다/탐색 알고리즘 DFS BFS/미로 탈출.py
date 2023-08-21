from collections import deque

N, M = map(int, input().split())
g = [ list(map(int, input())) for _ in range(N) ]

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

chk = [ [0] * M for _ in range(N) ]
chk[0][0] = 1

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs(y, x):
    global cnt
    dq = deque()
    dq.append((y, x))
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and g[ny][nx] == 1 and chk[ny][nx] == 0:
                chk[ny][nx] = chk[y][x] + 1
                dq.append((ny, nx))
    return chk[N-1][M-1]

print(bfs(0, 0))
