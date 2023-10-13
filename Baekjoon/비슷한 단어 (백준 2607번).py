import copy

N = int(input())
target = list(input())

ans = 0
for _ in range(N-1):
    target_cpy = copy.deepcopy(target)
    source = input()
    cnt = 0
    for s in source:
        if s in target_cpy:
            target_cpy.remove(s)
        else:
            cnt += 1

    if cnt <= 1 and len(target_cpy) <= 1:
        ans += 1

print(ans)
