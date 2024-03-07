# 프린터 큐

from collections import deque

x = int(input())
for i in range(x):
    q = list(map(int, input().split()))
    priority = deque(list(map(int, input().split())))
    ind = deque([i for i in range(q[0])])
    cnt = 0
    
    while priority:
        m = max(priority)
        
        if priority[0] < m:
            priority.append(priority.popleft())
            ind.append(ind.popleft())
        elif priority[0] == m:
            priority.popleft()
            cnt += 1
            if ind.popleft() == q[1]:
                print(cnt)
                break
