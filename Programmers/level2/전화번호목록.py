def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            m=min(len(phone_book[i]),len(phone_book[i]))
            if phone_book[i][0:m]==phone_book[j][0:m]:
                return False
    return True
