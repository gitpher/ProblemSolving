N, M = map(int, input().split())

res = [0] * M
cnt = 0

def dfs(lvl):
    global cnt
    if lvl == M:
        print(*res)
        cnt += 1
        return
    else:
        for i in range(N):
            res[lvl] = i + 1
            dfs(lvl + 1)


dfs(0)
print(cnt) # 총 경우의 수 = N ** M
