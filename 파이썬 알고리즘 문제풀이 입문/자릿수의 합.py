N = int(input())
a = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


max_val = 0
ans = 0
for x in a:
    tot = digit_sum(x)
    if max_val < tot:
        max_val = tot
        ans = x

print(ans)
