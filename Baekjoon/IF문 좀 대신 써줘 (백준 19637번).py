import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

level_name = list()
level_value = list()
for _ in range(N):
    name, value = input().rstrip().split()
    value = int(value)
    if level_value and level_value[-1] == value:
        continue
    level_name.append(name)
    level_value.append(value)

def binary_search(target):
    global level_name
    global level_value
    lt = 0
    rt = len(level_value) - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if level_value[mid] < target:
            lt = mid + 1
        else:
            rt = mid - 1
    return level_name[rt+1]

for _ in range(M):
    value = int(input().rstrip())
    print(binary_search(value))
