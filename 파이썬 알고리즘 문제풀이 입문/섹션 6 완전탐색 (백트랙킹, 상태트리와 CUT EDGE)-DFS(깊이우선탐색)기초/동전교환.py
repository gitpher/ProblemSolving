N = int(input())
a = list(map(int, input().split()))
M = int(input())

res = float('inf')
def dfs(lvl, sum):
    global res
    if sum == M:
        if res > lvl:
            res = lvl
            return
    else:
        for i in range(N):
            if sum + a[i] > M:
                return
            else:
                dfs(lvl + 1, sum + a[i])


dfs(0, 0)
print(res)
