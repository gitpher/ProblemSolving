def solution(numbers, target):
    cnt = 0
    def dfs(lvl, sum):
        nonlocal cnt
        if lvl == len(numbers):
            if sum == target:
                cnt += 1
            return
        else:
            dfs(lvl + 1, sum + numbers[lvl])
            dfs(lvl + 1, sum - numbers[lvl])

    dfs(0, 0)
    return cnt
