import sys

N = int(input())
a = list(map(int, input().split()))

tot = sum(a)

def dfs(lvl, sum):
    if sum > tot // 2: # tot의 절반보다 크면 이미 나머지 절반과 같은 값이 될 수 없음
        return

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
