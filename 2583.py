import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, y):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False

    global cnt

    if graph[x][y] == 0:
        graph[x][y] = 1
        cnt += 1
        dfs(x - 1, y)  # 상
        dfs(x, y - 1)  # 좌
        dfs(x + 1, y)  # 하
        dfs(x, y + 1)  # 우
        return True
    return False

lst = []
M, N, K = map(int, input().rstrip().split())

graph = [[0] * N for i in range(M)]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().rstrip().split())

    for j in range(x1, x2):
        for k in range(y1, y2):
            graph[k][j] = 1
graph.reverse()

result = 0
cnt = 0
for i in range(M):
    for j in range(N):
        if dfs(i, j) == True:
            result += 1
            lst.append(cnt)
            cnt = 0

print(result)
lst.sort()
[print(i, end=' ') for i in lst]