N = int(input())
a = [ list(map(int, input().split())) for _ in range(N) ]

a.insert(0, [0] * N)
a.append([0] * N)
for i in range(N + 2):
    a[i].insert(0, 0)
    a[i].append(0)

# a[i][j]
# 위쪽: a[i-1][j]   -1 0
# 아래쪽: a[i+1][j]  1 0
# 왼쪽: a[i][j-1]   0 -1
# 오른쪽: a[i][j+1]  0 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if all(a[i][j] > a[i+dy[k]][j+dx[k]] for k in range(4)):
            cnt += 1

print(cnt)

