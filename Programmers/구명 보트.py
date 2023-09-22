from collections import deque

def solution(people, limit):
    answer = 0
    
    people = deque(sorted(people))
    while people:
        answer += 1
        if len(people) == 1:
            break
        if people[0] + people[-1] > limit:
            people.pop()
        else:
            people.popleft()
            people.pop()
    
    return answer
