# 가장 긴 증가하는 부분 수열

N = int(input())

A = list(map(int, input().split()))

dp = [1 for i in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

