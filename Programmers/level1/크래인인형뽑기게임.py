def solution(board, moves):
    answer=0
    result = [0]
    for j in moves:
        for i in board:
            if i[j-1] != 0:
                if result[-1]==i[j-1]:
                    result.pop()
                    answer+=2
                else:
                    result.append(i[j-1])
                i[j-1]=0
                break
    
        
    return answer
