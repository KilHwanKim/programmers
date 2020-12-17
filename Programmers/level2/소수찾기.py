def is_prime_number(number):
    divisor = 1
    if number == 0:
        return False
    if number ==1:
        return False
    for j in range(1,(number+1)//2+1):
        if number%j==0:
            divisor+=1
        if divisor>2:
            return False
    return True
def solution(numbers):
    N_list = [int(x)for x in  numbers]
    L = len(N_list)
    answer=[]
    def perm(number,r):
        if number==r:
            prime= int("".join([str(x) for x in result]))
            if is_prime_number(prime) and prime not in answer:
                answer.append(prime)
        else :
            for i in range(L):
                if checklist[i] ==0:
                    result[number] = N_list[i]
                    checklist[i] = 1
                    perm(number+1,r)
                    checklist[i] = 0
    for i in range(1,L+1):
        
        checklist = [0]*len(N_list)
        result = [0]*i
        perm(0,i)
    return len(answer)
