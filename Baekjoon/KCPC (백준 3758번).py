import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    team_len, question_len, my_team_id, log_len = map(int, input().rstrip().split()) # 팀 개수, 문제 개수, 팀 ID, 로그 개수
    c = dict()
    for i in range(log_len):
        team_id, question_num, score_val = map(int, input().rstrip().split())
        if team_id in c:
            c[team_id][0][question_num] = max(c[team_id][0][question_num], score_val)
            c[team_id][2] += 1
            c[team_id][3] = i
        else:
            c[team_id] = [[0] * (question_len + 1), 0, 1, i] # question_score_list, score_val, submit_cnt, submit_time
            c[team_id][0][question_num] += score_val

    for v in c.values():
        v[1] = sum(v[0])

    for idx, val in enumerate(sorted(c.items(), key=lambda x: (-x[1][1], x[1][2], x[1][3]))):
        if val[0] == my_team_id:
            print(idx + 1)
