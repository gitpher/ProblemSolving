N, K = map(int, input().split())

olympic = []

for _ in range(N):
    country, gold, silver, bronze = map(int, input().split())
    olympic.append((country, gold, silver, bronze))

olympic.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 0
last = (0, 0, 0, 0)
for idx, val in enumerate(olympic):
    if not (last[1] == val[1] and last[2] == val[2] and last[3] == val[3]):
        rank = idx + 1

    if val[0] == K:
        print(rank)
        break

    last = val
