N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

a.extend(b)
a.sort()

print(*a)
