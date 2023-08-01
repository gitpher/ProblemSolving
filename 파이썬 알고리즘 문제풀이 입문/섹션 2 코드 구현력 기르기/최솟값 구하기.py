a = list(map(int, input().split()))

min_val = float('inf')
for i in range(len(a)):
    if a[i] < min_val:
        min_val = a[i]

print(min_val)
