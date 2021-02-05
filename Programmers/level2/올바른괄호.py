def solution(s):
    answer = True
    result = 0
    for val in list(s):
        if val==")":
            result-=1      
        else:
            result+=1
        if result <0:
            return False
    if result !=0:
        return False
    return True
