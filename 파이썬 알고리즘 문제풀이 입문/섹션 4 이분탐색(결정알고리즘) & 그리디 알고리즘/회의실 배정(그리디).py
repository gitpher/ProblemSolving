N = int(input())

a = []
for i in range(N):
    s, e = map(int, input().split())
    a.append((s, e))

a.sort(key=lambda x: (x[1], x[0]))

et = 0
cnt = 0
for s, e in a:
    if s >= et:
        et = e
        cnt += 1

print(cnt)
