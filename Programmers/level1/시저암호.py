def solution(s, n):
    answer = ''
    UP = list("abcdefghijklmnopqrstuvwxyz")
    LOW = list("abcdefghijklmnopqrstuvwxyz".upper())
    for i in list(s):
        if(i in UP):
            answer += UP[((UP.index(i)+n)%len(UP))]
        elif(i in LOW):
            answer += LOW[((LOW.index(i)+n)%len(LOW))]
        else:
            answer+= " "
    return answer
