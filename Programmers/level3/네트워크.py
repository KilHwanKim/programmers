
def bfs(computers,start,visited,answer):
    queue = []
    if visited[start]:
        return
    queue.append(start)
    visited[start] = True
    while queue :
        v = queue.pop(0)
        print(v,end=" ")
        for ind,val in enumerate(computers[v]):
            if (not visited[ind] )and (val==1):
                queue.append(ind)
                visited[ind] = True
    answer.append(1)
    
def solution(n, computers):
    visited = [False] *n
    answer=[]
    for i in range(n):
        bfs(computers,i,visited,answer)
    return  len(answer)
    
    
