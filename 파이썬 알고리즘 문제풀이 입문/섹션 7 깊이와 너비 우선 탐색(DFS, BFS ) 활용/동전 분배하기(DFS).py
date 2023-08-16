N = int(input())
a = list()
m = [0] * 3

for _ in range(N):
    a.append(int(input()))

min_val = float('inf')

def dfs(lvl):
    if lvl == N:
        global min_val
        dif = max(m) - min(m)
        if dif < min_val:
            s = set()
            for x in m:
                s.add(x)
            if len(s) == 3:
                min_val = dif
    else:
        for i in range(3):
            m[i] += a[lvl]
            dfs(lvl + 1)
            m[i] -= a[lvl]

dfs(0)
print(min_val)
