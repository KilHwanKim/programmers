def CanChange(word1,word2):
    L=len(word1)
    result=0
    for a,b in zip(list(word1),list(word2)):
        if a==b:
            result+=1
    if L-1==result:
        return True
    else:
        return False
def solution(begin, target, words):
    answer = 0
    anslist=[]
    checklist=[False]*len(words)
    Q = [[checklist,begin]]
    while Q:
        result = Q.pop(0)
        if result[1]==target:
            anslist.append(result[0].count(True))
        else:
            for index,val in enumerate(words):
                if CanChange(result[1],val) and not result[0][index]:
                    Q.append([result[0].copy(),val])
                    Q[-1][0][index]=True
    if anslist != []:
        answer = min(anslist)
    return answer
