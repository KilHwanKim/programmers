def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,1,2,4,5]
    num_score= [0,0,0]
    for index , a in enumerate(answers):
        if num1[index%5] == a:
            num_score[0] += 1 
        if num2[index%8] == a:
            num_score[1] += 1
        if num3[(int(index/2))%5] == a:
            num_score[2] +=1
    for a,j in enumerate(num_score):
        if j == max(num_score):
            answer.append(a+1)

    
    return answer
