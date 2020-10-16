def solution(s):
    answer = True
    s=s.lower()
    p=0
    y=0
    for i in s:
        if "p" ==i:
            p+=1
        if "y" ==i:
            y+=1
    if p!=y:
        answer = False
    return answer
