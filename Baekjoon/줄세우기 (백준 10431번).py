N = int(input())
for _ in range(N):
    arr = list(map(int, input().split()))
    T = arr.pop(0)

    cnt = 0
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] < arr[j]:
                cnt += 1

    print(T, cnt)
