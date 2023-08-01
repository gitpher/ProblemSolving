s = input()

a = ''
for c in s:
    if c.isdigit():
        a += c

b = int(a)
cnt = 0
for i in range(1, b+1):
    if b % i == 0:
        cnt += 1

print(b)
print(cnt)
