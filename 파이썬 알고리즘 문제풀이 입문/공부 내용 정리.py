import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

#===============================

import math
import collections
from itertools import combinations, permutations
from collections import deque
import heapq

#===============================

S = input()
N = int(input())
N, M = map(int, input().split())

a = range(N)
a = range(1, N + 1)
a = input().split()
a = list(map(int, input().split()))
a = list(map(int, str(N)))
a = [ list(map(int, input().split())) for _ in range(N) ]

a.sort(reverse=True)
a.sort(key=lambda x: (x[1], x[0])) # a.append((s, e))

#===============================

a = []
chk = []
stk = []
dq = deque(a)
hq = heapq.heappop(a) # heapq.heappush(a, n)
d = dict()
st = set()
cache = []

#===============================

min_val = float('inf')
max_val = float('-inf')

#===============================

def fun():
def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True
def reverse_digit(x):
    res = 0
    while x > 0:
        t = x % 10
        x = x // 10
        res = res * 10 + t
    return res
def digit_sum(x):
    res = 0
    while x > 0:
        res += x % 10
        x = x // 10
    return res

#===============================

lt = 0
rt = N - 1
while True:
    mid = (lt + rt) // 2
    if a[mid] == N:
        break
    elif a[mid] > N:
        rt = mid - 1
    else:
        lt = mid + 1

while lt <= rt:
    lt += 1
    rt -= 1


#===============================

dy = (0, 1, 0 ,-1)
dx = (1, 0, -1, 0)
for k in range(4):
    ny = y + dy[k]
    nx = x + dx[k]



#===============================
s = s[::-1]

''.join(map(str, a))
print(*a)




# 이분탐색 -------- list
# 그리디 ---------- list (+ tuple)
# 스택 ----------- list
# 큐 ------------- deque
# 해쉬 ----------- list
# 힙 ------------- heapq
# 딕셔너리 -------- dict
# DFS ----------- recursion (+ if else + for)
# BFS


# 중복 순열 :  chk 없음
# 순 열    : chk 있음  if chk[i] == 0 chk[i] = 1 dfs() chk[i] = 0
# 조 합    :chk 없음 dfs(lvl, s) for i in range(s, N + 1) cmb[lvl] = i dfs(lvl + 1, i + 1)

# 탐색 횟수 줄이는 방법
# 1. sort(reverse=True)
# 2. 밑에까지 보진 않는다 if sum + (tot - tsum) < max_val
# 3. 이항계수를 이용한다
# 4. 답만 얻으면 되는 것이면 sys.exit(0) 으로 브레이크
# 5. 스킵해야 하면 return

prm = []  # permutation
cmb = []  # combination
chk = []  # check
bno = []  # binomial coefficient

bno = [1] * N
for i in range(1, N - 1):
    bno[i] = bno[i - 1] * (N - i) // i

def dfs(lvl): dfs(0)
def dfs(lvl, sum): dfs(0, 0)
def dfs(lvl, sum, tsum): dfs(0, 0, 0)
def dfs(lvl, s): dfs(0, 1)



