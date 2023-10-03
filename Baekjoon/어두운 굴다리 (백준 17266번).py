N = int(input())
M = int(input())
lights = list(map(int, input().split()))

height = 0
if len(lights) > 1:
    for i in range(1, len(lights)):
        height = max(height, (lights[i] - lights[i-1] + 1) // 2)

print(max(height, lights[0], N - lights[-1]))
