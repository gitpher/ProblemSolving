N = int(input())

a = list(map(int, input().split()))

cnt = 0
sum = 0
for val in a:
    if val == 1:
       cnt += 1
       sum += cnt
    else:
        cnt = 0

print(sum)


