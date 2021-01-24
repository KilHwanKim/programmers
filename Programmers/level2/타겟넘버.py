def solution(numbers, target):
    answer=0
    L = len(numbers) ## numbers의 길이 
    
    for i in range(2**L):
        S = 0
        change = bin(i)[2::]
        result = (L-len(change))*"0"+change
        for index,sign in enumerate(list(result)):
            if sign =="0":
                S+= numbers[index]
            else :
                S -= numbers[index]
        if S==target:
            answer+=1
    return answer
