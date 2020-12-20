def solution(number, k):
    answer = number
    while True:
        if k==0:
            return answer ## k번 하면 정지
        sample = answer[1::]
        for x in range(1,len(str(answer))):
            if int(sample)< int(answer[0:x]+answer[x+1:]): # 제일 큰 수 구하기 
                sample = answer[0:x]+answer[x+1:] # 그 숫자를 제외한 수 
        answer = sample
        k-=1    
    return answer
