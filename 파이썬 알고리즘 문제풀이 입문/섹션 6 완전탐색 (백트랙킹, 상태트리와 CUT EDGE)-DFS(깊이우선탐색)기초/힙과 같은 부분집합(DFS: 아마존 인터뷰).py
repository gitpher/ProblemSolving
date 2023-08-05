import sys

N = int(input())
a = list(map(int, input().split()))

tot = sum(a)

ans = "NO"
def dfs(lvl, sum):
    if lvl == N:
        if sum == (tot - sum):
            print("YES")
            sys.exit(0)
            return
    else:
        dfs(lvl + 1, sum + a[lvl])
        dfs(lvl + 1, sum)

dfs(0, 0) # sys.exit(0)
print("NO")
