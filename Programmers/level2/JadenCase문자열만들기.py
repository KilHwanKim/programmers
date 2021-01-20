def solution(s):
    s=s.lower()
    answer = s[0].upper()
    sign=1
    for word in list(s[1::]):
        if sign==0:
            answer+=word.upper()
        else :
            answer+=word
        sign=1
        if word==" ":
            sign=0 
    return answer
