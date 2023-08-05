
N = int(input())
chk = [0] * (N + 1)

def dfs(v):
    if v == N + 1:
        for i in range(1, N + 1):
            if chk[i] == 1:
                print(i, end=' ')
        print()
    else:
        chk[v] = 1
        dfs(v + 1)
        chk[v] = 0
        dfs(v + 1)

dfs(1)
