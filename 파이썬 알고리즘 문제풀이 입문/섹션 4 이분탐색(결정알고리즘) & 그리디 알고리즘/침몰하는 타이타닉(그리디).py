from collections import deque

N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = deque(a)

# 실패한 방법
# cnt = 1
# tot = 0
# for w in a:
#     if tot + w > M:
#         cnt += 1
#         tot = w
#     else:
#         tot += w

# 내 방식으로 성공한 방법
# lt = 0
# rt = N - 1
# cnt = 0
# while lt <= rt:
#     if a[lt] + a[rt] <= M:
#         lt += 1
#         rt -= 1
#     else:
#         rt -= 1
#     cnt += 1

cnt = 0
while a:
    if len(a) == 1:
        break
    if a[0] + a[-1] > M:
        a.pop()
    else:
        a.popleft()
        a.pop()
    cnt += 1

print(cnt)
