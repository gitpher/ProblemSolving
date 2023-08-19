N, M = map(int, input().split())
g = [ list(map(int, input().split())) for _ in range(N) ]

hs = []
pz = []
for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            hs.append((i, j))
        elif g[i][j] == 2:
            pz.append((i, j))

cmb = [0] * M

city_min_dist = float('inf')
def dfs(lvl, s):
    global city_min_dist
    if lvl == M:
        sum = 0
        for j in range(len(hs)):
            hy, hx = hs[j]
            house_min_dist = float('inf')
            for idx in cmb:
                py, px = pz[idx]
                dist = abs(hy - py) + abs(hx - px)
                if dist < house_min_dist:
                    house_min_dist = dist
            sum += house_min_dist
        if sum < city_min_dist:
            city_min_dist = sum
    else:
        for i in range(s, len(pz)):
            cmb[lvl] = i
            dfs(lvl + 1, i + 1)

dfs(0, 0)
print(city_min_dist)
