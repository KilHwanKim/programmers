import math 
def solution(progresses, speeds):
    result = [-1]
    answer=[-1]
    for p,s in zip(progresses,speeds):
        days =math.ceil((100 - p)/s)
        out = max(days,result[-1])
        if out == result[-1]:
            answer[-1]+=1
        else:
            answer.append(1)
        result.append(out)
    return answer[1::]
