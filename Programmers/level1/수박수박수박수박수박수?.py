def solution(n):
    answer = ''
    result = list("수박")
    for i in range(n):
        answer+=result[i%2]
    return answer
