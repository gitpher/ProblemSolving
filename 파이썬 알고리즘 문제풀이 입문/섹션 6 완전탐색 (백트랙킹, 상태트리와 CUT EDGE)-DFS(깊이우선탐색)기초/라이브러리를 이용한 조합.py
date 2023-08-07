import itertools as it

N, K = map(int, input().split())
a = list(map(int, input().split()))
M = int(input())

cnt = 0
for cmb in it.combinations(a, K):
    if sum(cmb) % M == 0:
        cnt += 1

print(cnt)
