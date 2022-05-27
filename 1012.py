# 유기농 배추

import sys

sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


for _ in range(int(input())):
    n, m, k = map(int, input().split())

    graph = [[0] * n for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                result += 1
    print(result)