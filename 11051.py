import sys
sys.setrecursionlimit(10 ** 7)

cache = [[0] * 1001 for _ in range(1001)]


MOD = 10007

N, K = map(int, input().split())

def bino(n, k):
    if cache[n][k]:
        return cache[n][k]

    if k == 0 or k == n:
        cache[n][k] = 1
    else:
        cache[n][k] = bino(n-1, k-1) + bino(n-1, k)
        cache[n][k] %= 10007

    return cache[n][k]

print(bino(N, K))
