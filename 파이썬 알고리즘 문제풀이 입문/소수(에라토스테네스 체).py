N = int(input())

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

ans = 0
for i in range(2, N+1):
    if is_prime(i):
        ans += 1

print(ans)
