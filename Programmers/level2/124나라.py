def solution(n):
    answer = ''
    n-=1
    while True:
        if n<3:
            if n==0:
                return "1"+answer
            elif n==1:
                return "2"+answer
            else :
                return "4"+answer
        else:
            if n%3==0:
                answer="1"+answer
            elif n%3==1:
                answer="2"+answer
            else: 
                answer="4"+answer
            n=n//3-1
        
    
