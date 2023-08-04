import heapq as hq

a = []

while True:
    n = int(input())
    if n == -1:
        break

    if n == 0:
        if a:
            print(-hq.heappop(a)) # - 부호를 곱해서 출력하기
        else:
            print(-1)
    else:
        hq.heappush(a, -n) # - 부호를 곱해서 넣어주기


