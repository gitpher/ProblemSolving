T = int(input())
k = int(input())
cv = list()
cn = list()
for _ in range(k):
    v, n = map(int, input().split())
    cv.append(v)
    cn.append(n)
cnt = 0
def dfs(lvl, sum):
    global cnt
    if sum > T:
        return
    if lvl == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(cn[lvl] + 1):
            dfs(lvl + 1, sum + (i * cv[lvl]))
dfs(0, 0)
print(cnt)
