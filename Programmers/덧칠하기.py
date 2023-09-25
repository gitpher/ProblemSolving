def solution(n, m, section):
    ans = 0
    
    p = section[0] - 1
    for s in section:
        if s > p:
            p = s + m - 1
            ans += 1
    
    return ans
