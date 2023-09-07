from itertools import permutations

def solution(numbers):
    
    chrs = list(n for n in numbers)
    prms = []
    for i in range(1, len(chrs)+1):
        prms += list(permutations(chrs, i))
    nums = [int(''.join(n)) for n in prms]
    
    cand = []
    for n in nums:
        if n < 2:
            continue
        
        is_prime = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                is_prime = False
                break
        
        if is_prime:
            cand.append(n)
    
    return len(set(cand))
