N, M = map(int, input().split())
a = list(map(int, input().split()))

# 최소
# 용량

lt = max(a) # 최소 가장 큰 길이의 곡을 담을 수 있어야 함
rt = sum(a) # 모든 곡의 합을 M개의 CD가 담을 수 있어야 함

#용량
def fun(mid):
    tot = 0
    cnt = 1
    for l in a:
        if tot + l > mid:
            tot = l
            cnt += 1
        else:
            tot += l
    return cnt

#최소
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if fun(mid) <= M:
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(ans)
