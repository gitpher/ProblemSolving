N, M = map(int, input().split())

res = [0] * M
chk = [0] * (N + 1)
cnt = 0

def dfs(lvl): # lvl 0 1
    global cnt
    if lvl == M: # chk 이 꽉 찼을 때
        print(*res)
        cnt += 1
    else:
        for i in range(1, N + 1): # 1 2 3
            if chk[i] == 0:
                chk[i] = 1
                res[lvl] = i
                dfs(lvl + 1)
                chk[i] = 0


dfs(0)
print(cnt)
