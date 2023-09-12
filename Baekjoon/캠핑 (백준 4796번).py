import sys
input = sys.stdin.readline

i = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0:
        break

    print(f"Case {i}:", V // P * L + min(L, V % P))
    i += 1
