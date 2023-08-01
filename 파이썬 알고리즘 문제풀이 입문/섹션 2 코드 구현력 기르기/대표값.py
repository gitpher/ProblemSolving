N = int(input())
a = list(map(int, input().split()))

avg = round(sum(a) / N)

min_val = float('inf')
max_scr = 0
ans = 0

for idx, scr in enumerate(a):
    dif = abs(scr - avg)
    if dif <= min_val:
        min_val = dif
        if max_scr < scr:
            max_scr = scr
            ans = idx

print(f'{avg} {ans+1}')

'''
10
45 73 66 87 92 67 75 79 75 80
'''
