def solution(prices):
    ans = []
    
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        ans.append(cnt)
        
    return ans
