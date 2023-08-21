N = int(input())

a = list(map(int, input().split()))
a.insert(0, 0)

chk = [0] * (N + 1)
chk[1] = 1
res = 0

for i in range(2, N + 1):
    max_val = 0
    for j in range(i-1, 0, -1):
        if a[j] < a[i] and chk[j] > max_val:
            max_val = chk[j]
        chk[i] = max_val + 1
    if chk[i] > res:
        res = chk[i]

print(res)
