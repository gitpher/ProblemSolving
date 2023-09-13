games = {'Y': 1, 'F': 2, 'O': 3}
N, G = input().split()
gamers = set(input() for _ in range(int(N)))

print(len(gamers) // games[G])
