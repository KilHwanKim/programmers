def solution(n):
    num =1
    result ="";
    while  n>= 3**num:
        num+=1
    print(num)
    for i in range(num):
        result += str(n//3**(num-i-1))
        n = n%3**(num-i-1)
    answer = 0
    for a, i in enumerate(result):
         answer += int(i)*(3**a)
    return answer
