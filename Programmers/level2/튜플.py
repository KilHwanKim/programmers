def solution(s):
    result=[]
    answer=[]
    for i in s.split(",{"):
        i=i.strip("{")
        i=i.strip("}")
        result.append(i.split(","))
    result.sort(key = lambda x:len(x))
    for j in result:
        for t in j:
            if t not in answer:
                answer.append(t)
    return [int(x) for x in answer]
