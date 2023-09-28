N, K = map(int, input().split())

olympic = []

for _ in range(N):
    country, gold, silver, bronze = map(int, input().split())
    olympic.append((country, gold, silver, bronze))

olympic.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 0
for idx, val in enumerate(olympic):
    if val[1:] != olympic[idx-1][1:]:
        rank = idx + 1

    if val[0] == K:
        print(rank)
        break
