def solution(phone_number):
    answer = ''
    answer = phone_number.replace(phone_number[:-4:],"*"*len(phone_number[:-4:]))
    return answer
