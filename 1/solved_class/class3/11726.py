N = int(input())
dp = [0] * (N+2)
dp[1] = 1
dp[2] = 2
for i in range(2, N):
    dp[i+1] = dp[i] + dp[i-1]
print(dp[N] % 10007)