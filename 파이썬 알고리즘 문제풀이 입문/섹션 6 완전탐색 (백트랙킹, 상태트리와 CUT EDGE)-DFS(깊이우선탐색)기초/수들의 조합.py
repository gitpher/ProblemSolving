N, K = map(int, input().split())
a = list(map(int, input().split()))
M = int(input())

cmb = [0] * K
cnt = 0

def dfs(lvl, s, sum):
    global cnt
    if lvl == K:
        if sum % M == 0:
            cnt += 1
    else:
        for i in range(s, N):
            cmb[lvl] = a[i]
            dfs(lvl + 1, i + 1, sum + a[i])


dfs(0, 0, 0)
print(cnt)
