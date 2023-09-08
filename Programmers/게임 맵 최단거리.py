from collections import deque

def solution(maps):

    N = len(maps)
    M = len(maps[0])
    
    def is_valid_coord(y, x):
        return 0 <= y < N and 0 <= x < M
    
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    
    chk = [[0] * M for _ in range(N)]
    chk[0][0] = 1
    
    def bfs(y, x):
        dq = deque()
        dq.append((y, x))
        
        while dq:
            y, x = dq.popleft()
            
            for k in range(4):
                ny, nx = y+dy[k], x+dx[k]
                if is_valid_coord(ny, nx) and chk[ny][nx] == 0 and maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    dq.append((ny, nx))
        
    bfs(0, 0)
    
    if maps[N-1][M-1] == 1:
        return -1
    else:
        return maps[N-1][M-1]
