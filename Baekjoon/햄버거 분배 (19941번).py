N, K = map(int, input().split())
arr = list(input())

def is_valid_idx(i):
    return 0 <= i < N

cnt = 0
for i in range(N):
    if arr[i] == 'P':
        for j in range(i-K, i+K+1):
            if is_valid_idx(j) and arr[j] == 'H':
                arr[j] = 'E'
                cnt += 1
                break

print(cnt)
