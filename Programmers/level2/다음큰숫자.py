def solution(n):
    number= bin(n).count("1")
    n+=1
    while(number!=bin(n).count("1")):
        n+=1
    return n
