def solution(seoul):
    answer = '김서방은 '
    for a,i in enumerate(seoul):
        if i == "Kim":
            answer+= (str(a)+"에 있다")
    
    return answer
