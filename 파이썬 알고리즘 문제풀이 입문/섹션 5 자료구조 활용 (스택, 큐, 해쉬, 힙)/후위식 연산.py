e = input()
stk = []
for n in e:
    if n.isdecimal():
        stk.append(int(n))
    else:
        b = stk.pop()
        a = stk.pop()

        if n == '+':
            stk.append(a + b)
        elif n == '-':
            stk.append(a - b)
        elif n == '*':
            stk.append(a * b)
        elif n == '/':
            stk.append(a / b)

print(stk[0])
