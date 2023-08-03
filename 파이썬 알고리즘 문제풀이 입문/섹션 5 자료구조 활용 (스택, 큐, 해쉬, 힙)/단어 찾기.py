from collections import deque

N = int(input())
a = []
b = []

for _ in range(N):
    a.append(input())

for _ in range(N - 1):
    b.append(input())

c = set(a) - set(b)
print(c.pop())
