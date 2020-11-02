def solution(x):
    result= 0 
    for i in list(str(x)):
        result+= int(i)
    return  x%result==0
