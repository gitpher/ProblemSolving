ranks_len, new_score, cut_line = map(int, input().split())
if ranks_len > 0:
    ranks = list(map(int, input().split()))

    if ranks_len == cut_line and ranks[-1] >= new_score:
        print(-1)
    else:
        res = ranks_len + 1
        for i in range(ranks_len):
            if ranks[i] <= new_score:
                res = i + 1
                break
        print(res)
else:
    print(1)
