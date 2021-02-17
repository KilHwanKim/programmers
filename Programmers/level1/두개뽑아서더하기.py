def solution(numbers):
    answer = []
    result1 = numbers.copy()
    while result1:
        M = result1.pop(0)
        result2 = result1.copy()
        while result2:
            N = result2.pop(0)
            answer.append(M+N)
    return sorted(list(set(answer)))
