K = int(input())
a = list(map(int, input().split()))
tot = sum(a)
res = set(range(1, max(a)))


def dfs(lvl, sum):
    if lvl == K:
        res.add(sum)
    else:
        dfs(lvl + 1, sum + a[lvl])
        dfs(lvl + 1, sum)


dfs(0, 0)

print(tot - len(res))
