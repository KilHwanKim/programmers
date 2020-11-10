def solution(s):
    result = []
    for i in s.split(" "):
        answer = ''
        for a,j in enumerate(i):
            if a%2!=0:
                answer+=j.lower()
            else:
                answer+=j.upper()
        result.append(answer)
    return " ".join(result)
