#s = input()
#
# a = ''
# for c in s:
#     if c.isdigit():
#         a += c
#
# b = int(a)
# cnt = 0
# for i in range(1, b+1):
#     if b % i == 0:
#         cnt += 1
#
# print(b)
# print(cnt)


s = input()

res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)

cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1

print(f'{res}\n{cnt}')
