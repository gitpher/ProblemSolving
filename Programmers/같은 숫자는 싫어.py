def solution(arr):
    answer = []
    
    chk = [10]
    for x in arr:
        if x != chk[0]:
            answer.append(x)
            chk[0] = x
    
    return answer
