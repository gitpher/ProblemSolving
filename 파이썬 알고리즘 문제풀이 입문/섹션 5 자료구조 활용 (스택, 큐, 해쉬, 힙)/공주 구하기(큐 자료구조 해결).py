from collections import deque
N, K = map(int, input().split())
a = list(range(1, N + 1))
a = deque(a)

for i in range(N - 1):
    for j in range(K - 1):
        a.append(a.popleft())
    a.popleft()

from collections import deque
N, K = map(int, input().split())
a = list(range(1, N + 1))
a = deque(a)

for i in range(N - 1):
    for j in range(K - 1):
        a.append(a.popleft())
    a.popleft()

print(a[0])

# while a:
#     for _ in range(K - 1):
#         a.append(a.popleft())
#     a.popleft()
#     if len(a) == 1:
#         print(a[0])
#         a.popleft()

