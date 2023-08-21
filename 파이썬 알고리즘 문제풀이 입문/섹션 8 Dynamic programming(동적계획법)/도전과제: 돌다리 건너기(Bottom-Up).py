N = int(input())

chk = [0] * (N + 2)
chk[1] = 1
chk[2] = 2

for i in range(3, N + 2):
    chk[i] = chk[i - 1] + chk[i - 2]

print(chk[N + 1])
