from collections import deque
N = 7

g = [ list(map(int, input().split())) for _ in range(N) ]
chk = [ [0] * 7 for _ in range(N) ]

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

def bfs(s_y, s_x):
    dq = deque()
    dq.append((s_y, s_x))
    while dq:
        y, x = dq.popleft()
        g[y][x] = 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and g[ny][nx] == 0:
                g[ny][nx] = 1
                chk[ny][nx] = chk[y][x] + 1
                dq.append((ny, nx))

    return -1 if chk[N - 1][N - 1] == 0 else chk[N - 1][N - 1]

print(bfs(0, 0))
