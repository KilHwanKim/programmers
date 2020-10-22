def solution(n):
    answer = []
    for i in str(n)[::-1]:
        answer.append(int(i))
    
    return answer
