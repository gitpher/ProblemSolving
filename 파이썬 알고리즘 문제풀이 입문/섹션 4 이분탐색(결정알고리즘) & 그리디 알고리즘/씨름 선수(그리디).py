N = int(input())

a = []
for i in range(N):
    h, w = map(int, input().split())
    a.append((h, w))

a.sort(reverse=True)

lw = 0
cnt = 0
for h, w in a:
    if w > lw:
        lw = w
        cnt += 1

print(cnt)
