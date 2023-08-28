def solution(participant, completion):

    a = dict()

    for p in participant:
        if p in a:
            a[p] += 1
        else:
            a[p] = 1

    for c in completion:
        a[c] -= 1

    for k, v in a.items():
        if v == 1:
            return k
