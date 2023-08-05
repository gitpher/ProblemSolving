C, N = map(int, input().split())

a = []
for i in range(N):
    a.append(int(input()))

b = []

def dfs(lvl, sum):

    if lvl == N:
        b.append(sum)
        return
    else:
        if sum + a[lvl] > C:
            b.append(sum)
            return
        else:
            dfs(lvl + 1, sum + a[lvl])
            dfs(lvl + 1, sum)

dfs(0, 0)
print(max(b))
