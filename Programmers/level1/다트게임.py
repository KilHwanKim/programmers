def solution(dartResult):
    option ="#*"
    SDT = "SDT"
    answer = []
    number=""
    for i in list(dartResult):
        if i in SDT:
            if i == "S":
                answer.append(int(number))
            elif i == "D":
                answer.append(int(number)**2)
            else :
                answer.append(int(number)**3)
            number=""
        elif i in option:
            if i == "#":
                answer[-1]*=-1
            else:
                answer[-2::]=[2*x for x in answer[-2::]]
                print(answer)
        else:
            number+=i
    return sum(answer)
