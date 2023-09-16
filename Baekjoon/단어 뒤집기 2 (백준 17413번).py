from collections import deque
import sys
S = sys.stdin.readline().rstrip() + ' '
dq = deque()
ans = ''

rev = True
for s in S:
    if s == '<':
        rev = False
        while dq:
            ans += dq.pop()

    dq.append(s)

    if s == '>':
        rev = True
        while dq:
            ans += dq.popleft()
        continue

    if s == ' ' and rev:
        dq.pop()
        while dq:
            ans += dq.pop()
        ans += ' '

print(ans)
