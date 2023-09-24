def solution(wallpaper):
    
    N = len(wallpaper)
    M = len(wallpaper[0])
    
    lux = N
    luy = M
    rdx = 0
    rdy = 0
    
    for i in range(N):
        for j in range(M):
            if wallpaper[i][j] == '#':
                if i < lux:
                    lux = i
                if j < luy:
                    luy = j
                if i + 1 > rdx:
                    rdx = i + 1
                if j + 1 > rdy:
                    rdy = j + 1
    
    return [lux, luy, rdx, rdy]
