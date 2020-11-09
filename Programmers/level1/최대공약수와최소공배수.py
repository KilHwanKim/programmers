def solution(n, m):
    nm = n*m
    answer = []
    result = 1
    while result!=0:
        result = n%m
        n= m
        m=result
    answer.append(n)
    answer.append(int(nm/n))
    return answer
