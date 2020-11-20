def solution(A,B):
    return  sum([x[0]*x[1] for x in zip(sorted(A,reverse=True),sorted(B))])
