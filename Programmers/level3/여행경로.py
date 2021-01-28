def solution(tickets):
    FT = [False] * len(tickets)
    answer = ["ICN"]
    Q=1
    while Q :
        Q=[]
        for index, val in enumerate(tickets):
            if (not FT[index])  and val[0]==answer[-1]:
                Q.append([index,val[1]])
        if Q==[]:
            return answer
        Q.sort(key = lambda x : x[-1] )
        FT[Q[0][0]] =True
        answer.append(Q[0][-1]) 
