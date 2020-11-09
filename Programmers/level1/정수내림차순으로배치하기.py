def solution(n):
    answer = 0
    answer = int("".join(sorted(list(str(n)),reverse=True)))
    return answer
