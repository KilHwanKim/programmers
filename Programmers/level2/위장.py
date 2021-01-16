def solution(clothes):
    result = {}
    answer=1
    for x in clothes:
        if x[1] in result.keys():
            result[x[1]]+=1
        else:
            result[x[1]]=1
    for y in result.values():
        answer*=(y+1)
    return answer-1
