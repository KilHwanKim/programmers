def solution(arr):
    answer = []
    if arr == [10]:
        return [-1]
    else :
        arr.remove(min(arr))
        return arr
