# 1, 2, 3 더하기

dp = [0,1,2,4,0,0,0,0,0,0,0] 
for i in range(int(input())):
    n = int(input())
    if n == 1 or n == 2 or n == 3:
        print(dp[n])
    else:
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[n])
