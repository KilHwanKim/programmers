def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key = lambda x: (x[0],x[1%len(x)],x[2%len(x)],x[3%len(x)]),reverse =True) 
    return str(int("".join(numbers)))
