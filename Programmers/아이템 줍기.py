from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):

    field = [[-1] * 102 for i in range(102)]

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] != 0:
                    field[i][j] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    dq.append([characterX * 2, characterY * 2])
    chk = [[1] * 102 for i in range(102)]

    ans = 0
    while dq:
        x, y = dq.popleft()
        if x == itemX * 2 and y == itemY * 2:
            ans = chk[x][y] // 2
            break
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if field[nx][ny] == 1 and chk[nx][ny] == 1:
                dq.append([nx, ny])
                chk[nx][ny] = chk[x][y] + 1

    return ans
