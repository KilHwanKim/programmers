def solution(participant, completion):
    participant.sort()
    completion.sort()
    for x,y in zip(participant, completion):
        if x!= y:
            return x
    return participant[-1]
