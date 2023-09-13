import sys
input = sys.stdin.readline

K = int(input())
stk = [0]

for i in range(K):
    n = int(input())
    if n:
        stk.append(n)
    else:
        stk.pop()

print(sum(stk))
