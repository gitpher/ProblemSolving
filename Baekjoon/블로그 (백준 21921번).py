from collections import deque
import sys
input = sys.stdin.readline

N, X = map(int, input().rstrip().split())
visits = list(map(int, input().rstrip().split()))

dq = deque()
cur_visit_sum = 0
max_visit_sum = 0
max_visit_cnt = 0
for v in visits:
    dq.append(v)
    cur_visit_sum += v

    if len(dq) > X:
        cur_visit_sum -= dq.popleft()

    if cur_visit_sum > max_visit_sum:
        max_visit_sum = cur_visit_sum
        max_visit_cnt = 1
    elif cur_visit_sum == max_visit_sum:
        max_visit_cnt += 1

print("SAD") if max_visit_sum == 0 else print(f"{max_visit_sum}\n{max_visit_cnt}")
