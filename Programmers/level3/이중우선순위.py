import heapq as hp
def solution(operations):
    heap = []
    for val in operations:
        if val == "D 1":
            if heap!=[]:
                heap.remove(max(heap))
        elif val == "D -1":
            if heap!=[]:
                hp.heappop(heap)
        else :
            hp.heappush(heap,int(val.split(" ")[-1]))
    if heap==[]:
        return [0,0]
    return [max(heap),min(heap)]
