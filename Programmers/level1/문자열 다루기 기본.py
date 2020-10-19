def solution(s):
    answer = True
    if (len(s)!=4 and len(s)!=6 ):
        answer = False
    else:
        for i in list(s):
            if i not in "0123456789":
                answer = False
    return answer
