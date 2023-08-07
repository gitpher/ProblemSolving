N, M = map(int, input().split())

g = [ [0] * (N + 1) for _ in range(N + 1) ]

for _ in range(M):
    y, x, v = map(int, input().split())
    g[y][x] = v

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(g[i][j], end=' ')
    print()
