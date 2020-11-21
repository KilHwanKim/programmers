def solution(n):
    answer =1;
    for x in range(1,n):
        i=1
        while (sum(range(x,x+i))<=n):
            if(sum(range(x,x+i))==n):
                answer+=1
            i+=1
    return answer
