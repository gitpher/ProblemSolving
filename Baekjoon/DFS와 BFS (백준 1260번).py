from collections import deque

# N = 정점 개수, M = 간선 개수, V = 시작 정점
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for x in sorted(graph[v]):
        if visited[x] == 0:
            dfs(x)

dfs(V)

print()

visited = [0] * (N+1)
def bfs(v):
    dq = deque()
    dq.append(v)
    visited[v] = 1
    while dq:
        v = dq.popleft()
        print(v, end=' ')
        for x in sorted(graph[v]):
            if visited[x] == 0:
                visited[x] = 1
                dq.append(x)
bfs(V)
