def solution(s):
    L = len(s)
    answer =len(s)
    for unit in range(1,L+1):
        result = [[1,""]]
        for i in range(0,L,unit):
            if result[-1][1]!=s[i:i+unit]:
                result.append(["",s[i:i+unit]])
            else:
                if result[-1][0]=="":
                    result[-1][0]=2
                else:
                    result[-1][0]+=1
        if answer> len("".join([str(x[0])+x[1] for x in result[1::]])):
            answer=len("".join([str(x[0])+x[1] for x in result[1::]]))
    return answer
