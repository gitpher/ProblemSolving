import sys
sys.setrecursionlimit(10**7)

T = int(input())

def dfs(start, current, arr, visited):
    visited[current] = 1
    next = arr[current] - 1
    if visited[next] == 0:
        dfs(start, next, arr, visited)

for _ in range(T):
    ans = 0
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [0] * N
    for i in range(N):
        start = i
        if visited[start] == 0:
            dfs(start, start, arr, visited)
            ans += 1
    print(ans)
