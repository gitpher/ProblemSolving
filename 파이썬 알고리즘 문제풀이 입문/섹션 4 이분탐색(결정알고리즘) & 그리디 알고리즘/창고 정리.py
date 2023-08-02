L = int(input())
a = list(map(int, input().split()))
M = int(input())

# for m in range(M):
#     min_val = min(a)
#     min_idx = a.index(min_val)
#     max_val = max(a)
#     max_idx = a.index(max_val)
#
#     a[min_idx] += 1
#     a[max_idx] -= 1
#
# print(max(a) - min(a))

a.sort()
for _ in range(M):
    a[0] += 1
    a[-1] -= 1
    a.sort()
print(a[-1] - a[0])
