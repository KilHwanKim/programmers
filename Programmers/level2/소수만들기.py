def isprime(number):
    sign = False
    for k in range(2,number-1):
        
        if number%k==0:
            return sign
    return True
def solution(nums):
    answer=0
    for x in range(len(nums)-2):
        
        for y in range(x+1,len(nums)-1):
        
            for z in range(y+1,len(nums)):
                    if isprime(nums[x]+nums[y]+nums[z]):
                        answer+=1
                
    return answer    

                
