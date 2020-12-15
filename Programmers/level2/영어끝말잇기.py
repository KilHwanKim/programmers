def solution(n, words):
    answer = []
    L = len(words)
    for i in range(1,L):
        if words[i] in words[0:i]:
            return (i+1)%n==0 and [n,(i+1)//n] or [(i+1)%n,(i+1)//n+1]
        if words[i][0] !=words[i-1][-1]:
            return (i+1)%n==0 and [n,(i+1)//n] or [(i+1)%n,(i+1)//n+1]
    return [0,0]
