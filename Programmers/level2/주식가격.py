def solution(prices):
    L = len(prices)
    answer =[0]*L
    for index in range(L):
        for i in range(index+1,L):
            answer[index]+=1
            if prices[index]>prices[i]:
                break  
    return answer
