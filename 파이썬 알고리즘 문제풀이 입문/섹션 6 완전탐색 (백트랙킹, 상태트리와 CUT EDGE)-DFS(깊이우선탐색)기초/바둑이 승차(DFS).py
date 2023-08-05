C, N = map(int, input().split())

a = []
for i in range(N):
    a.append(int(input()))

# b = []
# def dfs(lvl, sum):
#     if lvl == N:
#         b.append(sum)
#         return
#     else:
#         if sum + a[lvl] > C:
#             b.append(sum)
#             return
#         else:
#             dfs(lvl + 1, sum + a[lvl]) # 경우 1
#             dfs(lvl + 1, sum) # 경우 2
# dfs(0, 0)
# print(max(b))

tot = sum(a)
res = float('-inf')
def dfs(lvl, sum, tsum):
    global tot
    global res

    if sum + (tot - tsum) < res: # 지금까지의 선택과 나머지 선택의 합이 지금 가진 답보다 작다면 더 볼 필요 없음
        return
    if sum > C:
        return
    if lvl == N:
        if sum > res:
            res = sum
    else:
        dfs(lvl + 1, sum + a[lvl], tsum + a[lvl])
        dfs(lvl + 1, sum, tsum + a[lvl])

dfs(0, 0, 0)
print(res)
