T = int(input())
for _ in range(T):
    N = int(input())
    ranks = list(map(int, input().split()))

    teams = dict()
    for team in ranks:
        if team in teams:
            teams[team][0] += 1
        else:
            teams[team] = [1, []] # 팀원 수, 점수 리스트

    team_of_six = [k for k, v in teams.items() if v[0] == 6]

    rank = 1
    for team in ranks:
        if team in team_of_six:
            teams[team][1].append(rank)
            rank += 1

    min_team = 0
    min_score = float('inf')
    for key, value in teams.items():
        if value[0] == 6:
            team_score = sum(value[1][:4])
            if team_score < min_score:
                min_score = team_score
                min_team = key
            elif team_score == min_score:
                team_score_a = sum(value[1][:5])
                team_score_b = sum(teams[min_team][1][:5])
                if team_score_a < team_score_b:
                    min_team = key

    print(min_team)
