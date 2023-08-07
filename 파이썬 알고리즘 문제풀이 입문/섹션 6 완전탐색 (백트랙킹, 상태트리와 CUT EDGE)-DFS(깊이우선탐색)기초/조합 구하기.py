N, M = map(int, input().split())

cmb = [0] * M
chk = [0] * (N + 1)


cnt = 0
def dfs(lvl, r):
    global cnt
    if lvl == M:
        cnt += 1
        print(*cmb)
    else:
        for i in range(r, N + 1):
            if chk[i] == 0:
                chk[i] = 1
                cmb[lvl] = i
                dfs(lvl + 1, r + i)
                chk[i] = 0


dfs(0 ,1)
print(cnt)
