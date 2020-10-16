def solution(s):
    answer = ''
    result = sorted(list(s),reverse = True) 
    for i in result:
        answer+=i
    return answer
