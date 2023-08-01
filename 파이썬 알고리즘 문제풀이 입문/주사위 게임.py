N = int(input())

max_val = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    tmp.sort()
    a, b, c = tmp[0], tmp[1], tmp[2]

    res = 0
    if a == b and b == c:
        res = 10000 + a * 1000
    elif a == b or a == c:
        res = 1000 * a + 100
    elif b == c:
        res = 1000 * b + 100
    else:
        res = max(a, b, c) * 100

    if res > max_val:
        max_val = res

print(max_val)
