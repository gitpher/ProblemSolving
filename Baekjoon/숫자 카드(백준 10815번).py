from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

ans = []

for n in numbers:
    ans.append(1 if (bisect_right(cards, n) - bisect_left(cards, n)) > 0 else 0)
print(*ans)
