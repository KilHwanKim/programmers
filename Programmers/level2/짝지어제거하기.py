def solution(s):
    result =[0]
    for i in list(s):
        if result[-1]==i:
            result.pop()
        else:
            result.append(i)
    return result ==[0] and 1 or 0
