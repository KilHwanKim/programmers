def solution(number, k):
    stack=[number[0]]
    for i in list(number)[1::]:
        while stack and stack[-1]<i and k>0:
            stack.pop()
            k-=1
        else:
            stack.append(i)
    return "".join(stack[:len(number)-k])
