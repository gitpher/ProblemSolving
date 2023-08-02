K, N = map(int, input().split())

a = []
res = 0

max_val = 0
for i in range(K):
    tmp = int(input())
    a.append(tmp)
    if tmp > max_val:
        max_val = tmp

lt = 1
rt = max_val

max_len = 0
while lt <= rt:
    mid = (lt + rt) // 2 # 숫자 (인덱스 아님)
    cnt = 0
    for i in range(K):
        cnt += a[i] // mid
    print(cnt)

    if cnt == N:
        if mid > max_len:
            max_len = mid
            lt = mid + 1
        else:
            rt = mid - 1

    elif cnt < N:
        rt = mid - 1
    else:
        lt = mid + 1

print(max_len)
