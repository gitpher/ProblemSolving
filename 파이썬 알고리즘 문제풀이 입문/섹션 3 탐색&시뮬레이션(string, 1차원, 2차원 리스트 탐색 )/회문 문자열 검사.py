N = int(input())

a = []

for i in range(N):
    s = input()
    s = s.lower()
    t = list(s)
    t.reverse()
    r = ''.join(t)

    if s == r:
        a.append(f'#{i+1} YES')
    else:
        a.append(f'#{i+1} NO')

for p in a:
    print(p)

