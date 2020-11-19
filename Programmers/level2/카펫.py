def solution(brown, yellow):
    Y= [(yellow//x,x) for x in range(1,int(((yellow)**0.5))+1) if yellow%x==0]
    by = brown +yellow
    BY = [(by//x,x) for x in range(1,int(((by)**0.5))+1) if by%x==0]
    for i in Y:
        for j in BY:
            if i[0]+2 ==j[0] and  i[1]+2 ==j[1]:  
                return j
