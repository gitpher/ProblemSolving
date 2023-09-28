N = int(input())

people = []
for i in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))

for a in people:
    rank = 1
    for b in people:
        if a[0] < b[0] and a[1] < b[1]:
            rank += 1
    print(rank, end=' ')
