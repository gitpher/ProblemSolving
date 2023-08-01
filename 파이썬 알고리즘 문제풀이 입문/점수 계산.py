N = int(input())

a = list(map(int, input().split()))

acc = 0
res = 0
for val in a:
    if val == 1:
       acc += 1
       res += acc * val
    else:
        acc = 0

print(res)


