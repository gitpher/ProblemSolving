N = int(input())
t = list()
p = list()

for _ in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)
t.insert(0, 0)
p.insert(0, 0)

res = 0

def dfs(lvl, p_sum):
    global res
    if lvl == N + 1:
        if p_sum > res:
            res = p_sum
    else:
        if lvl + t[lvl] <= N + 1:
            dfs(lvl + t[lvl], p_sum + p[lvl])
        dfs(lvl + 1, p_sum)

dfs(1, 0)
print(res)
