S = list(reversed(input()))
z, o = S.count('0') // 2, S.count('1') // 2
for _ in range(z):
    S.remove('0')
S.reverse()
for _ in range(o):
    S.remove('1')

print(''.join(S))
