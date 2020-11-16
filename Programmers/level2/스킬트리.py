def solution(skill, skill_trees):
    answer = len(skill_trees)
    for x in skill_trees:
        result = []
        i=0
        for j in list(x):
            if j in skill:
                result.append(skill.index(j))
                if i !=skill.index(j):
                    answer-=1
                    break
                i +=1
    return answer
