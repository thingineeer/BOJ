import sys
sys.setrecursionlimit(10**4)

def dfs_R(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 'R':
        graph[x][y] = 'C'
        dfs_R(x-1,y)
        dfs_R(x,y-1)
        dfs_R(x+1,y)
        dfs_R(x,y+1)
        return True
    return False

def dfs_G(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 'G':
        graph[x][y] = 'C'
        dfs_G(x-1,y)
        dfs_G(x,y-1)
        dfs_G(x+1,y)
        dfs_G(x,y+1)
        return True
    return False

def dfs_B(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 'B':
        graph[x][y] = 'C'
        dfs_B(x-1,y)
        dfs_B(x,y-1)
        dfs_B(x+1,y)
        dfs_B(x,y+1)
        return True
    return False

def dfs_R_G(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph2[x][y] == 'R' or graph2[x][y] == 'G':
        graph2[x][y] = 'C'
        dfs_R_G(x-1,y)
        dfs_R_G(x,y-1)
        dfs_R_G(x+1,y)
        dfs_R_G(x,y+1)
        return True
    return False

def dfs_B2(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    
    if graph2[x][y] == 'B':
        graph2[x][y] = 'C'
        dfs_B2(x-1,y)
        dfs_B2(x,y-1)
        dfs_B2(x+1,y)
        dfs_B2(x,y+1)
        return True
    return False

result = 0
n = int(input())
graph = []
graph2 = []

for _ in range(n):
    k = input()
    graph.append(list(k))
    graph2.append(list(k))
    
#RGB
    
for i in range(n):
    for j in range(n):
        if dfs_R(i,j):
            result += 1
            
for i in range(n):
    for j in range(n):
        if dfs_G(i,j):
            result += 1

for i in range(n):
    for j in range(n):
        if dfs_B(i,j):
            result += 1
            
print(result, end = ' ')
result = 0

#RRB

for i in range(n):
    for j in range(n):
        if dfs_R_G(i,j):
            result += 1

for i in range(n):
    for j in range(n):
        if dfs_B2(i,j):
            result += 1

            
print(result)


