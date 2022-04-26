import sys
input = sys.stdin.readline
 
N = int(input())
 
A = [int(input()) for i in [0]*N]
 
dp = [1] * N
 
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
 
print(N-max(dp))