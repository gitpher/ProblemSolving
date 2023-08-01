a = list(range(1, 21))

# s = 5 # idx = 4, -16   (5 - 20 - 1)
# e = 10 # idx = 9, -11   (10 - 20 - 1)

for j in range(10):
    s, e = map(int, input().split())
    l = e - s + 1

    for i in range(l // 2):
        a[s-1+i], a[e-1-i] = a[e-1-i], a[s-1+i]

print(*a)
