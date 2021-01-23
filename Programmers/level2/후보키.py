from itertools import combinations
def IsUnique(tup,relation):
    result = []
    for i in relation:
        IN =[]
        for j in tup:
            IN.append(i[j])
        if IN in result:
            return False
        else :
            result.append(IN)
    return True
def IsMin(tup,result):
    result = list(result)
    tup = set(tup)
    for i in result:
        i = set(i)
        if i == i.intersection(tup):
            return False 
    return True
def solution(relation):
    result = []
    column = len(relation[0])
    row = len(relation)
    for i in range(1,column+1):
        for j in combinations(range(column),i):
            if (IsUnique(j,relation)) and (IsMin(j,result)):
                result.append(j)
    return len(result)
