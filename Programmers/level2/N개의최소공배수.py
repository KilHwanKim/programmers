def LCM(n, m):
    nm = n*m
    result = 1
    while result!=0:
        result = n%m
        n= m
        m=result
    return nm/n
def solution(arr):
    number = arr[0]
    for i in arr[1::]:
        number= LCM(number,i)
    return number
