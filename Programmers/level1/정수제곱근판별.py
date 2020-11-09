def solution(n):
    answer = -1
    for i in range(1,int(n**0.5)+1):
        if i**2==n:
            answer = (i+1)**2
            break
    return int(answer)
