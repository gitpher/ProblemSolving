a = input()
b = input()

c = dict()

for x in a:
    c[x] = c.get(x, 0) + 1

for x in b:
    c[x] = c.get(x, 0) - 1

for x in a:
    if c.get(x) > 0:
        print("NO")
        break
else:
    print("YES")
