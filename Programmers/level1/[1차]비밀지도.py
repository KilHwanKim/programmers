def solution(n, arr1, arr2):
    answer= []
    result1 = [format(x,'b').zfill(n) for x in arr1]
    result2 = [format(y,'b').zfill(n) for y in arr2]
    for a,b in zip(result1,result2):
        result = ""
        for x,y in zip(list(a),list(b)):
            if((x=='1') | (y=='1')):
                result+="#"
            else:
                result+=" "
        answer.append(result)
    return answer
