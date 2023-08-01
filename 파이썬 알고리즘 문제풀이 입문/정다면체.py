N, M = map(int, input().split())

length = N + M
a = [0] * length

for n in range(1, N+1):
    for m in range(1, M+1):
        a[n+m] += 1

max_val = max(a)

for i in range(length + 1):
    if a[i] == max_val:
        print(i, end=' ')
