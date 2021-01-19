def solution(s):
    answer = [0,0]
    while s!="1":
        zero =s.count("0")
        one = s.count("1")
        answer[1]+=zero
        s= bin(one)[2::]
        answer[0]+=1
    return answer
