N = int(input())
a = list(map(int, input().split()))

# def reverse(x):
#     a = list(str(x))
#     a.reverse()
#     return int(''.join(a))

def reverse(x): # 5050
    res = 0
    while x > 0:
        t = x % 10
        x = x // 10
        res = res * 10 + t
    return res

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for val in a:
    res = reverse(val)
    if isPrime(res):
        print(res, end=' ')
