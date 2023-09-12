N = M = 10
g = [ list(map(int, input().split())) for _ in range(N)]

ans = 25
paper = [0] * 6 # 인덱스는 색종이 크기

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def is_possible(y, x, sz):
    if paper[sz] == 5:
        return False

    if not is_valid_coord(y, x):
        return False

    for i in range(sz):
        for j in range(sz):
            if g[y+i][x+j] == 0:
                return False

    return True

def mark(y, x, sz, val):
    for i in range(sz):
        for j in range(sz):
            g[y+i][x+j] = val

    if val == 0:
        paper[sz] += 1
    else:
        paper[sz] -= 1

def backtracking(y, x):
    global ans
    if y == 10:
        ans = min(ans, sum(paper))
        return

    if x == 10:
        backtracking(y+1, 0)
        return

    if g[y][x] == 0:
        backtracking(y, x+1)
        return

    for sz in range(1, 6):
        if is_possible(y, x, sz):
            mark(y, x, sz, 0)
            backtracking(y, x+1)
            mark(y, x, sz, 1)

backtracking(0, 0)

print(-1 if ans == 25 else ans)
