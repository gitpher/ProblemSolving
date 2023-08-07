import sys

N, F = map(int, input().split())

per = [0] * N # permutation
bin = [1] * N # binomial coefficient # cache
chk = [0] * (N + 1) # check

for i in range(1, N - 1):
    bin[i] = bin[i-1] * (N - i) // i # 지난 숫자의 N-1을 곱하기 (N - i)는 갈수록 작아지는 수 i는 커지는 수

def dfs(lvl, sum):
    if lvl == N and sum == F:
        print(*per)
        sys.exit(0)
    else:
        for i in range(1, N + 1): # i는 4까지의 숫자
            if chk[i] == 0: #만약 중복이 없으면
                chk[i] = 1
                per[lvl] = i
                dfs(lvl + 1, sum + per[lvl] * bin[lvl]) #
                chk[i] = 0

dfs(0, 0)
