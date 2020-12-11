def solution(people, limit):
    people.sort()
    heavy = len(people)-1
    light=0
    answer =0
    while light<=heavy:
        if people[heavy]+people[light]<=limit:
            heavy -=1
            light+=1
        else:
            heavy-=1
        answer+=1
    return answer
