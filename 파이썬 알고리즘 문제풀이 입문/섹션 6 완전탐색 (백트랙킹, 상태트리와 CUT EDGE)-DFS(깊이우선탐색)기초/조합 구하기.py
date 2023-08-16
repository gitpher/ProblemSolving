N, M = map(int, input().split())

cmb = [0] * M

cnt = 0
def dfs(lvl, s):
    global cnt
    if lvl == M:
        cnt += 1
        print(*cmb)
    else:
        for i in range(s, N + 1):
            cmb[lvl] = i
            dfs(lvl + 1, i + 1)


dfs(0, 1)
print(cnt)
