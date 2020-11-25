import re
def solution(files):
    answer = []
    for i in files:
        answer.append(re.split("([0-9]+)",i))    
    answer.sort(key =lambda x :(x[0].lower(), int(x[1])) )
    return ["".join(x) for x in answer]
