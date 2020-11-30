def solution(m, musicinfos):
    answer = []
    for x in musicinfos:
        result = x.split(",")
        time = (int(result[1].split(":")[0])-int(result[0].split(":")[0]))*60+(int(result[1].split(":")[1])-int(result[0].split(":")[1]))
        code = []
        for x in list(result[3]):
            if x=="#":
                code.append("*"+code.pop()) 
            else:
                code.append(x)
        answer.append((result[2]," ".join([code[x%len(code)] for x in range(time)])))
    listen=[]
    for x in m:
            if x=="#":
                listen.append("*"+listen.pop()) 
            else:
                listen.append(x)
    listen = " ".join(listen)
    for x in answer:
        if listen in x[1]:
            return x[0]
    return "'(none')"
