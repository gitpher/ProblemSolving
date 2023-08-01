N = int(input())
a = [ list(map(int, input().split())) for _ in range(N) ]
M = int(input())

for i in range(M):
    r, d, n = map(int, input().split())
    if d == 0:
        for _ in range(n):
            t = a[r-1].pop(0)
            a[r-1].append(t)
    else:
        for _ in range(n):
            t = a[r-1].pop()
            a[r-1].insert(0, t)

sum = 0
s = 0
e = N - 1
for i in range(N):
    for j in range(s, e + 1):
        sum += a[i][j]
    if i < N // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(sum)
