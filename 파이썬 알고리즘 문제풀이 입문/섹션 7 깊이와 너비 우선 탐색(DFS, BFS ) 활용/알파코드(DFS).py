code = list(map(int, input()))

n = len(code)
code.insert(n, -1)

res = [0] * n
cnt = 0

def dfs(lvl, pos):
    global cnt
    global res
    if lvl == n:
        cnt += 1
        for i in range(pos):
            print(chr(res[i] + 64), end='')
        print()
    else:
        for i in range(1, 27):
            if code[lvl] == i:
                res[pos] = i
                dfs(lvl + 1, pos + 1)
            elif i >= 10 and code[lvl] == i // 10 and code[lvl + 1] == i % 10:
                res[pos] = i
                dfs(lvl + 2, pos + 1)

dfs(0, 0)
print(cnt)
