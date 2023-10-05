N = int(input())
dist = list(map(int, input().split()))
gas = list(map(int, input().split()))

min_gas = gas[0]
tot_gas = 0

for i in range(N-1):
    if min_gas > gas[i]:
        min_gas = gas[i]

    tot_gas += min_gas * dist[i]

print(tot_gas)
