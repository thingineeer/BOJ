# 11279 최대힙

import heapq
import sys
input = sys.stdin.readline
h = []
for i in range(int(input().rstrip())):
    x = int(input())
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(-heapq.heappop(h)) # point
    else: 
        heapq.heappush(h,-x) # point