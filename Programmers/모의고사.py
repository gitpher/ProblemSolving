def solution(answers):
    res = []
    
    spo1 = [1, 2, 3, 4, 5]
    spo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    spo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scr1 = scr2 = scr3 = 0
    for i in range(len(answers)):
        if spo1[i%5] == answers[i]:
            scr1 += 1
        if spo2[i%8] == answers[i]:
            scr2 += 1
        if spo3[i%10] == answers[i]:
            scr3 += 1
    
    mx = max(scr1, scr2, scr3)
    if scr1 == mx:
        res.append(1)
    if scr2 == mx:
        res.append(2)
    if scr3 == mx:
        res.append(3)
    
    return res
