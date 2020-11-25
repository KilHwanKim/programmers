def solution(record):
    answer =[]
    IDBook = {}
    for x in record:
        result =x.split(" ")
        if result[0] =="Enter":
            answer.append([result[1],"님이 들어왔습니다."])
            IDBook[result[1]]=result[2]
        elif result[0] == "Change":
            IDBook[result[1]]=result[2]
        else:
            answer.append([result[1],"님이 나갔습니다."])
    return [IDBook[x[0]]+x[1]for x in answer ]
