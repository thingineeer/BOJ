# BFS
# 브루트 포스

import sys
import copy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_spaces(lab):
    empty_spaces = []
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == 0:
                empty_spaces.append((i, j))
    return empty_spaces


def bfs():
    queue = deque()

    temp_lab = copy.deepcopy(lab)

    for i in range(N):
        for j in range(M):
            if temp_lab[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 0인 경우 바이러스 퍼트림
            if temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                queue.append((nx, ny))

    cnt = 0

    for i in range(N):
        cnt += temp_lab[i].count(0)

    return cnt


empty_spaces = find_spaces(lab)

result = 0
for i in range(len(empty_spaces)):
    for j in range(i + 1, len(empty_spaces)):
        for k in range(j + 1, len(empty_spaces)):
            a, b, c = [empty_spaces[i], empty_spaces[j], empty_spaces[k]]
            lab[a[0]][a[1]], lab[b[0]][b[1]], lab[c[0]][c[1]] = 1, 1, 1
            cnt = bfs()
            result = max(result, cnt)
            lab[a[0]][a[1]], lab[b[0]][b[1]], lab[c[0]][c[1]] = 0, 0, 0

print(result)
