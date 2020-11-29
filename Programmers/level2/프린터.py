def solution(priorities, location):
    answer =[]
    flag = True
    while flag:
        for a,i in enumerate(priorities):
            if priorities.count(0) ==len(priorities):
                flag = False
                break
            if max(priorities)==i:
                answer.append(a)
                priorities[a]=0
        
    return answer.index(location)+1
