def solution(s, skip, index):
    answer = ""
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    for ch in skip: 
        if ch in alpha:
            alpha = alpha.replace(ch, "")
    
    for i in s:
        answer += alpha[(alpha.index(i) + index) % len(alpha)] 
    
    return answer
