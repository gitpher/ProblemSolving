N, M = map(int, input().split())

pv = []
pt = []

for _ in range(N):
    a, b = map(int, input().split())
    pv.append(a)
    pt.append(b)

chk = [0] * N

max_val = float('-inf')
def dfs(lvl, val, time):
    global max_val
    if time > M:
        return
    if lvl == N:
        if val > max_val:
            max_val = val
    else:
        dfs(lvl + 1, val + pv[lvl], time + pt[lvl])
        dfs(lvl + 1, val, time)

dfs(0, 0, 0)
print(max_val)
