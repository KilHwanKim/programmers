def solution(n):
    answer = 0
    result = []
    for i in range(1,n+1):
        if n%i==0:
            result.append(i)
    answer = sum(result)
    return answer
