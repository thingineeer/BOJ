import copy
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if x < 0 or y < 0 or y >= N or x >= N:
        return False

    if native_graph[x][y] == 1:
        native_graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

Max = 0
result = 0
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

native_graph = copy.deepcopy(graph)

for k in range(1, max(max(native_graph)) + 1):
    for i in range(N):
        for j in range(N):
            if native_graph[i][j] >= k:
                native_graph[i][j] = 1
            else:
                native_graph[i][j] = 0

    result = 0
    for i in range(N):
        for j in range(N):
            if dfs(i, j):
                result += 1

    if Max < result:
        Max = result

    native_graph = copy.deepcopy(graph) # graph 초기화

print(Max)