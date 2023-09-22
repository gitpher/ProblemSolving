from itertools import permutations

def solution(number, k):
    
    stk = []
    
    for num in number:
        while k > 0 and stk and stk[-1] < num:
            stk.pop()
            k -= 1
        stk.append(num)
    
    return ''.join(stk[0:len(number)-k])
