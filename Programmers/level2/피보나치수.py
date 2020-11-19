def solution(n):
    answer =[0,1]
    for i in range(1,n):
        answer.append(answer[i]+answer[i-1])
    return answer[-1]%1234567
