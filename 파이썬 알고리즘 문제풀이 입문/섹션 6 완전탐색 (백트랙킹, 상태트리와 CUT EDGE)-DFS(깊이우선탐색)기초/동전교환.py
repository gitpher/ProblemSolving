N = int(input())
a = list(map(int, input().split()))
M = int(input())

a.sort(reverse=True) # 가장 적은 수의 동전 갯수를 구해야 하기 떄문에 큰 단위부터

res = float('inf')
# def dfs(lvl, sum):
#     global res
#     if sum == M:
#         if res > lvl:
#             res = lvl
#             return
#     else:
#         for i in range(N):
#             if sum + a[i] > M:
#                 return
#             else:
#                 dfs(lvl + 1, sum + a[i])
def dfs(lvl, sum):
    global res
    if sum > M:
        return

    if sum == M:
        if res > lvl:
            res = lvl
    else:
        for i in range(N):
            dfs(lvl + 1, sum + a[i])


dfs(0, 0)
print(res)
