N = int(input())

chk = [0] * (N + 1)

def dfs(lvl):
    if lvl == 1 or lvl == 2:
        return lvl

    if chk[lvl] != 0:
        return chk[lvl]

    chk[lvl] = dfs(lvl - 1) + dfs(lvl - 2)
    return chk[lvl]

print(dfs(N))
