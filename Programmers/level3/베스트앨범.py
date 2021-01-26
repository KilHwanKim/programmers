def solution(genres, plays):
    answer={}
    result = {}
    for index,GP in enumerate(zip(genres,plays)):
        if GP[0] in answer.keys():
            answer[GP[0]]+=GP[1]
            result[GP[0]].append((index,GP[1]))
        else:
            answer[GP[0]]=GP[1]
            result[GP[0]]=[(index,GP[1])]
    
    L = list(answer.keys())
    L.sort(key = lambda x: answer[x],reverse=True)  
    A=[]
    for k in L:
        result[k].sort(key = lambda x: (x[1],x),reverse=True)
        
        A+=[i[0] for i in result[k][:2]]
    return A
