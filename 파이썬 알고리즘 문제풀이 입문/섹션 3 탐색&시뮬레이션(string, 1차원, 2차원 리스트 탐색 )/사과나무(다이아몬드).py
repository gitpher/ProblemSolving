N = int(input())
a = [ list(map(int, input().split())) for _ in range(N) ]

# a[0][2]
# a[1][1] a[1][2] a[1][3]
# a[2][0] a[2][1] a[2][2] a[2][3] a[2][4]
# a[3][1] a[3][2] a[3][3]
# a[4][2]

sum = 0
s = e = N // 2

for i in range(N):
    for j in range(s, e+1):
        sum += a[i][j]
    if i < N // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(sum)
