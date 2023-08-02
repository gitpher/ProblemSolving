N = int(input())
a = list(map(int, input().split()))

ans = [0] * N

for i in range(N): # a
    for j in range(N): # ans j는 포인터
        if a[i] == 0 and ans[j] == 0:
            ans[j] = i + 1
            break
        elif ans[j] == 0:
            a[i] -= 1

print(*ans)
