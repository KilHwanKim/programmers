def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if i<=budget:
            budget-=i
            answer+=1
    return answer
