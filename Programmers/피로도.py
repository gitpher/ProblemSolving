def solution(k, dungeons):
    
    N = len(dungeons)
    chk = [0] * N
    
    ans = 0
    def dfs(k, cnt):
        nonlocal ans
        ans = max(ans, cnt)
        
        for i in range(N):
            if chk[i] == 0 and k >= dungeons[i][0]:
                chk[i] = 1
                dfs(k-dungeons[i][1], cnt+1)
                chk[i] = 0
    
    dfs(k, 0)
    return ans
