import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

c = dict()
for _ in range(N):
    word = input().rstrip()
    word_len = len(word)
    if word_len >= M:
        if word in c:
            c[word][0] += 1
        else:
            c[word] = [1, word_len]

for x in sorted(c.items(), key=lambda x: (-x[1][0], -x[1][1], x[0])):
    print(x[0])
