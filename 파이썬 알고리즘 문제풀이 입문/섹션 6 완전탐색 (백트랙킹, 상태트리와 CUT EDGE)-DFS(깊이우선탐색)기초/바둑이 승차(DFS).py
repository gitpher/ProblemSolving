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


res = float('-inf')
def dfs(lvl, sum):
    global res

    if sum > C:
        return
    if lvl == N:
        if sum > res:
            res = sum
    else:
        dfs(lvl + 1, sum + a[lvl])
        dfs(lvl + 1, sum)

dfs(0, 0)
print(res)
