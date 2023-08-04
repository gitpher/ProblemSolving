import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())

def dfs(x):
    if x == 0:
        return
    else:
        dfs(x // 2)
        print(x % 2, end='')

dfs(N)
