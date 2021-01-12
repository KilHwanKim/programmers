def solution(bridge_length, weight, truck_weights):
    B = [0 for x in range(bridge_length)] ## 다리길이
    t = 0 # 시간
    S= 0# 다리의 합 ## sum 함수를 썼을 시 시간 불합격
    while True:
        if S==0 and truck_weights==[]:## 종료조건 다리도 0 남은 트럭 줄도 0일때 종료
            return t
        else :
            t+=1 ### 시간 흐름
            S-=B[-1]
            B.pop() ## 다리 마지막 제거 (트럭이 지나감)
            if truck_weights==[]:
                B= [0]+ B # 
            elif S+truck_weights[0] <= weight:
                S+=truck_weights[0]
                B = [truck_weights.pop(0)]+B   
            else :
                B= [0]+ B
