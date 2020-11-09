def solution(n):
    answer = 0
    result = list(range(0,n+1))
    result[0] = 1
    i = 2
    while i <= (n**0.5):
        if result[i] ==1:
            i+=1
            continue
        else :
            j = 2
            while  j*i<=n:
                result[j*i]=1
                j+=1
            i+=1
    answer = n - result.count(1) +1
    return answer
