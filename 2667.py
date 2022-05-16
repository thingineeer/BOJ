# 단지번호 붙이기

lst = []
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        lst.append(0)
        dfs(x-1, y) # 상
        dfs(x, y-1) # 좌
        dfs(x+1, y) # 하
        dfs(x, y+1) # 우
        return True
    return False
    
result = 0
result_cnt = []
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            result += 1
            result_cnt.append(len(lst))
            lst = []
            
print(result)
result_cnt.sort()
[print(i) for i in result_cnt]