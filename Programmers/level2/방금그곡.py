def solution(m, musicinfos):
    answer = []
    for x in musicinfos:
        result = x.split(",")
        start =result[0].split(":")
        end = result[1].split(":")
        title = result[2]
        code = result[3].replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
        time = (int(end[0])-int(start[0]))*60+(int(end[1])-int(start[1]))
        code_song = "".join([code[x%len(code)] for x in range(time)])
        answer.append((title,code_song))       
    M_song = m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
    for an in answer:
        if M_song in an[1]:
            return an[0]
        
    return "(None)"
