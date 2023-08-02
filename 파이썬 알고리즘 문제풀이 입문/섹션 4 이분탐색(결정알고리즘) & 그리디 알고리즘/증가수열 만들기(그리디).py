N = int(input())
a = list(map(int, input().split()))

lt = 0
rt = N - 1
ln = 0
s = ""

while lt <= rt:
    if a[lt] > ln:
        ln = a[lt]
        s += 'L'
        lt += 1
    else:
        lt += 1

    if a[rt] > ln:
        ln = a[rt]
        s += 'R'
        rt -= 1
    else:
        rt -= 1


print(f'{len(s)}\n{s}')
