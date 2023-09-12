from itertools import combinations

N, M = map(int, input().split())

houses = []
chickens = []

for i in range(N):
    for j, val in enumerate(map(int, input().split())):
        if val == 1:
            houses.append((i, j))
        elif val == 2:
            chickens.append((i, j))

def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

ans = 2 * N * len(houses)
for cmb in combinations(chickens, M):
    tot = 0
    for h in houses:
        tot += min(get_dist(h, c) for c in cmb)

    ans = min(ans, tot)

print(ans)
