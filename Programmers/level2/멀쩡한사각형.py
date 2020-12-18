import math
def solution(w,h):
    answer =w*h
    remove = 0
    if h<w:
        h,w = w,h
    for i in range(w):
        end = math.ceil((i+1)*h/w)
        start= math.floor((i) *h/w)
        remove +=end - start
        if ((i+1) *h /w) %1==0:
            return answer -(remove * w/ (i+1))
    return answer-remove
