def solution(p):
    result=0
    tag = "u"
    S = ""
    answer = []
    for i in list(p):
        if i=="(":
            result+=1
        else :
            result-=1
        S+=i
        if result <0:
            tag = "v"
        if result == 0:
            answer.append([tag,S])
            S=""
            tag = "u"        
    for j in range(len(answer)):
        if answer[j][0]=="v":
            L = len(answer[j][1])//2
            print(L)
            answer[j][1] = ("("*L)+(")"*L)
            
    return "".join([x[1] for x in answer])
