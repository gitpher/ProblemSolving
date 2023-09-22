C = int(input())
P = int(input())

network = [[] for _ in range(C+1)]

for _ in range(P):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = [0] * (C+1)

def dfs(c, net):
    visited[c] = 1
    for cc in net[c]:
        if visited[cc] == 0:
            dfs(cc, net)

dfs(1, network)
print(sum(visited)-1)
