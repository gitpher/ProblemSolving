import itertools as it

N, F = map(int, input().split())

bno = [1] * N
for i in range(1, N - 1):
    bno[i] = bno[i - 1] * (N - i) // i

a = list(range(1, N + 1))

cnt = 0
for prm in it.permutations(a):
    sum = 0
    for idx, val in enumerate(prm):
        sum += val * bno[idx]
    if sum == F:
        print(*prm)
        break
