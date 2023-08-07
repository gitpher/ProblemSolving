N, M = map(int, input().split())

g = [ [0] * (N + 1) for _ in range(N + 1) ] # 간선이 연결되어 있는지 확인
chk = [0] * (N + 1) # 중복 제거
chk[1] = 1 # 1번 노드 방문 했다는 뜻
path = []
path.append(1)

for i in range(M):
    y, x = map(int, input().split())
    g[y][x] = 1

cnt = 0
def dfs(v):
    global cnt
    global path
    if v == N:
        cnt += 1
        print(*path)
    else:
        for i in range(1, N + 1):
            if chk[i] == 0 and g[v][i] == 1:
                chk[i] = 1
                path.append(i)
                dfs(i) # i 로 이동했으니 i vertex로 레벨 변경
                path.pop()
                chk[i] = 0


dfs(1)
print(cnt)
