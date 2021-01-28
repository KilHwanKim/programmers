def solution(tickets):
    answer = []
    start = "ICN"
    Q= []
    result = []
    for i in tickets:
        if start == i[0]:
            Q.append([i])
    while Q :
        v = Q.pop(0)
        if len(v) == len(tickets):
            answer.append(v)
        else :
            start = v[-1][-1]
            for i in tickets:
                vc = v.copy()
                if start == i[0] and (vc.count(i)<tickets.count(i)) :
                    vc.append(i)
                    Q.append(vc)
    for i in answer:
        R=[]
        for j in i:
            R.append(j[0])
        R.append(i[-1][-1])
        result.append(R)
        
    result.sort(key= lambda x: str(x))
    return result[0]
