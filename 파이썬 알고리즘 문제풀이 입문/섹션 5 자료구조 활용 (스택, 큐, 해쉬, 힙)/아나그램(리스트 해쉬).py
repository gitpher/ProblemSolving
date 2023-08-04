a = input()
b = input()

c = [0] * 52 # 알파벳 26자 * 2
d = [0] * 52

for x in a:
    if x.isupper():
        c[ord(x) - 65] += 1
    else:
        c[ord(x) - 71] += 1

for x in b:
    if x.isupper():
        d[ord(x) - 65] += 1
    else:
        d[ord(x) - 71] += 1

for i in range(52):
    if c[i] != d[i]:
        print("NO")
        break
else:
    print("YES")
