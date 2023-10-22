import sys
import heapq

N = int(input())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
