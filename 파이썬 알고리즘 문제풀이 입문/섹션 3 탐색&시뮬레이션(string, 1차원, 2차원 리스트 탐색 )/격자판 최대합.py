N = int(input())

a = [ list(map(int, input().split())) for _ in range(N) ]

# 가로 줄 a[0][0] a[0][1] a[0][2] a[0][3] a[0][4]
# 세로 줄 a[0][0] a[1][0] a[2][0] a[3][0] a[4][0]
# 대각선 줄 a[0][0] a[1][1] a[2][2] a[3][3] a[4][4], a[0][4] a[1][3] a[2][2] a[3][1] a[4][0]

max_val = float('-inf') # ans
for i in range(N):
    sum1 = sum2 = 0
    for j in range(N):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > max_val:
        max_val = sum1
    if sum2 > max_val:
        max_val = sum2

sum1 = sum2 = 0
for i in range(N):
    sum1 += a[i][i]
    sum2 += a[i][N-1-i]
    if sum1 > max_val:
        max_val = sum1
    if sum2 > max_val:
        max_val = sum2

print(max_val)

