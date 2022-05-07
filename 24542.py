# 튜터-튜티 관계의 수

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)

def bfs(v):
    visited[v] = 1
    lst.append(0)
    q = deque()
    q.append(v)

    while q:
        p = q.popleft()
        for next_p in graph[p]:
            if not visited[next_p]:
                q.append(next_p)
                visited[next_p] = 1
                lst.append(0)

cnt = 1
lst = []
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        cnt *= len(lst)
        lst = []

print(cnt % 1000000007)