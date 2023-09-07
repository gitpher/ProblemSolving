from itertools import product

def solution(word):
    
    a = ['A', 'E', 'I', 'O', 'U']
    prod = []
    for i in range(1, len(a)+1):
        prod += [''.join(p) for p in list(product(a, repeat=i))] 
    prod.sort()
    
    return prod.index(word) + 1
