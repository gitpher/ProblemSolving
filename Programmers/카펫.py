def solution(brown, yellow):

    deno = []
    area = brown + yellow
    for i in range(1, area + 1):
            if area % i == 0:
                deno.append([i, area // i])
    
    for w, h in deno:
        if (w - 2) * (h - 2) == yellow:
            return [max(w, h), min(w, h)]
