import sys
input = sys.stdin.readline

dp = [0] * 101
dp[0] = dp[1] = dp[2] = 1

for i in range(int(input())):
    n = int(input())
    if n < 3:
        print(dp[n])
    else:
        for i in range(n-2):
            dp[i+3] = dp[i] + dp[i+1]
        print(dp[n-1])
