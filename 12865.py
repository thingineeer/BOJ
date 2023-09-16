import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
dp = [0] * (K+1)
for _ in range(N):
    W, V = map(int, input().rstrip().split())
    for i in range(K, W-1, -1):
        dp[i] = max(dp[i], dp[i-W] + V)
print(dp[K])
