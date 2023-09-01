def solution(genres, plays):
    
    a = list()
    b = dict()
    for i in range(len(plays)):
        a.append([genres[i], plays[i], i])
        if genres[i] in b:
            b[genres[i]] += plays[i]
        else:
            b[genres[i]] = plays[i]
    a.sort(key=lambda x : (x[0], -x[1], x[2])) # 플레이순 고유번호순
    b = sorted(b.items(), key=lambda x: -x[1]) # 장르순

    res = list()
    for k in b:
        cnt = 0
        for x in a:
            if k[0] == x[0] and cnt < 2:
                res.append(x[2])
                cnt += 1
    return res
