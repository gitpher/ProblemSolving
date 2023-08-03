N = int(input())
# a = []
# b = []
#
# for _ in range(N):
#     a.append(input())
#
# for _ in range(N - 1):
#     b.append(input())
#
# c = set(a) - set(b)
# print(c.pop())

a = dict()
for i in range(N):
    a[input()] = 1

for j in range(N - 1):
    a[input()] = 0

for key, val in a.items():
    if val == 1:
        print(key)
