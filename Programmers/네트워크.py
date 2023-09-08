def solution(n, computers):
    chk = [0] * n
    
    def dfs(c):
        for i in range(len(computers[c])):
            if computers[c][i] == 1 and chk[i] == 0:
                chk[i] = 1
                dfs(i)
    
    ans = 0
    for idx, val in enumerate(computers):
        if chk[idx] == 0:
            chk[idx] = 1
            dfs(idx)
            ans += 1
    
    return ans
