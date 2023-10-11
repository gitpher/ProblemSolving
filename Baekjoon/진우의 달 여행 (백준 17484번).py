import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = [ list(map(int, input().rstrip().split())) for _ in range(N) ]

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

dy = (1, 1, 1)
dx = (-1, 0, 1)

min_fuel = float('inf')
def dfs(y, x, s, d):
    global min_fuel

    if y == N - 1:
        min_fuel = min(min_fuel, s)
    else:
        for k in range(3):
            if k is not d:
                ny = y + dy[k]
                nx = x + dx[k]
                if is_valid_coord(ny, nx):
                    dfs(ny, nx, s + board[ny][nx], k)

for i in range(M):
    dfs(0, i, board[0][i], -1)

print(min_fuel)
