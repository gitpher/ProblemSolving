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

dy = (0, 1, 0 ,-1)=
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
