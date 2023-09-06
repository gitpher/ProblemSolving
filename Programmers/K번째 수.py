def solution(array, commands):
    
    res = []
    for c in commands:
        i, j, k = c[0], c[1], c[2]
        a = array[i-1:j]
        a.sort()
        res.append(a[k-1])
        
    return res
