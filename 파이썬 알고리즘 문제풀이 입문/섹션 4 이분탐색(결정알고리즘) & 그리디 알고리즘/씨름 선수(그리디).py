N = int(input())

a = []
for i in range(N):
    h, w = map(int, input().split())
    a.append((h, w))

a.sort(reverse=True)

lh = 0
lw = 0
cnt = 0
for h, w in a:
    if h > lh or w > lw:
        lh = h
        lw = w
        cnt += 1

print(cnt)
