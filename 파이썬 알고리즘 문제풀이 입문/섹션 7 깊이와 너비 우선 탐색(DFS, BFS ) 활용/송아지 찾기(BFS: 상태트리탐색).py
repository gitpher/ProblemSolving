from collections import deque

MAX = 10_000
chk = [0] * (MAX + 1)
dist = [0] * (MAX + 1)

S, E = map(int, input().split())

chk[S] = 1
dist[S] = 0
dq = deque()
dq.append(S)

while dq:
    now = dq.popleft()
    if now == E:
        break
    for nxt in (now - 1, now + 1, now + 5):
        if 0 < nxt < MAX:
            if chk[nxt] == 0:
                dq.append(nxt)
                chk[nxt] = 1
                dist[nxt] = dist[now] + 1 # lvl의 역할

print(dist[E])
