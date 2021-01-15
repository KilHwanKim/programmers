def solution(arr1, arr2):
    answer = []
    for y in range(len(arr1)):
        A=[]
        for x in range(len(arr2[0])):
            S=0
            for z in range(len(arr1[y])):
                S+=arr1[y][z]*arr2[z][x]
            A.append(S)
        answer.append(A)
    return answer
