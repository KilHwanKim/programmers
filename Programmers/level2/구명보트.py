def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    ship=0
    while people:
        ship=people[0]
        del people[0]
        for index in range(len(people)):
            if people[index]+ship<=limit:
                del people[0]
                break  
        answer+=1
    return answer
