N, C = map(int, input().split())
a = []
for i in range(N):
    a.append(int(input()))
a.sort()

# N 마구간 갯수
# C 말 마릿수


# 가까운 두 말의 최대 거리

# 입력: 거리
# 출력: 말의 수
def fun(d):
    cnt = 1
    lp = a[0]
    for i in range(1, N):
        if a[i] - lp >= d:
            cnt += 1
            lp = a[i]

    return cnt


lt = 1
rt = a[-1]

res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if fun(mid) >= C:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
